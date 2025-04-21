import cv2
import mediapipe as mp
import serial
import struct
import time
import numpy as np

class ArmController:
    def __init__(self, port='COM4', baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        self.current_angles = [90, 0, 90, 45]  # [base, keeper, tilt, pan]

    def send_angles(self, angles):
        angles = [
            max(0, min(180, int(angles[0]))),    # Base (0-180)
            max(0, min(8, int(angles[1]))),      # Keeper (0-8)
            max(35, min(120, int(angles[2]))),   # Tilt (35-120)
            max(0, min(60, int(angles[3])))      # Pan (0-60)
        ]
        self.current_angles = angles
        data = struct.pack('4B', *angles)
        self.ser.write(data)
    
    def close(self):
        self.ser.close()

def count_fingers(hand_landmarks, hand_label):
    # จุด landmark สำคัญ
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    
    # ตรวจสอบนิ้วโป้ง 
    if hand_label == "Left":
        thumb_extended = thumb_tip.x > thumb_ip.x  # มือซ้ายให้นิ้วโป้งทางขวาเป็น extended
    else:
        thumb_extended = thumb_tip.x < thumb_ip.x  # มือขวานิ้วโป้งทางซ้ายเป็น extended
    
    # นับนิ้วที่เหลือ (นิ้วชี้ถึงนิ้วก้อย)
    other_fingers = 0
    for tip_id, pip_id in [(8, 6), (12, 10), (16, 14), (20, 18)]:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[pip_id].y:
            other_fingers += 1
    
    return (1 if thumb_extended else 0) + other_fingers

def calculate_angles(left_hand, right_hand, left_label, right_label):
    angles = arm.current_angles[:]  # ใช้มุมปัจจุบันเป็นค่าเริ่มต้น
    
    # ควบคุมด้วยมือซ้าย
    if left_hand:
        fingers = count_fingers(left_hand, left_label)
        wrist_x = left_hand.landmark[mp_hands.HandLandmark.WRIST].x
        wrist_y = left_hand.landmark[mp_hands.HandLandmark.WRIST].y
        
        if fingers >= 4:  # 4 นิ้วขึ้นไป = ควบคุมฐาน (แกน X)
            angles[0] = int((1 - wrist_x) * 180)
        elif fingers == 3:  # 3 นิ้ว = ควบคุม Pan (แกน Y)
            angles[3] = int(wrist_y * 60)  # ปรับช่วงเป็น 0-60

    # ควบคุมด้วยมือขวา
    if right_hand:
        fingers = count_fingers(right_hand, right_label)
        wrist_x = right_hand.landmark[mp_hands.HandLandmark.WRIST].x
        wrist_y = right_hand.landmark[mp_hands.HandLandmark.WRIST].y
        
        # ควบคุม Gripper
        angles[1] = 0 if fingers <= 1 else 8  # 1 นิ้วหรือน้อยกว่า = กำมือ
        
        if fingers >= 0:  # 4 นิ้วขึ้นไป = ควบคุม Tilt (แกน Y)
            angles[2] = int(120 - (wrist_y * 85))  # ปรับช่วงเป็น 120-35
    
    return angles

# ตั้งค่า MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_drawing = mp.solutions.drawing_utils

# โปรแกรมหลัก
cap = cv2.VideoCapture(0)
arm = ArmController()

try:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
            
        image = cv2.flip(image, 1)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        left_hand = None
        right_hand = None
        left_label = ""
        right_label = ""
        
        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = handedness.classification[0].label
                
                # วาด landmark มือ
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                    mp.solutions.drawing_styles.get_default_hand_connections_style()
                )
                
                # แสดงจำนวนนิ้ว
                fingers = count_fingers(hand_landmarks, hand_label)
                coords = (int(hand_landmarks.landmark[0].x * image.shape[1]), 
                         int(hand_landmarks.landmark[0].y * image.shape[0]))
                
                color = (121, 44, 250) if hand_label == "Left" else (54, 180, 34)
                cv2.putText(image, f"{hand_label}: {fingers}", 
                          (coords[0]-50, coords[1]-30), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                
                if hand_label == "Left":
                    left_hand = hand_landmarks
                    left_label = "Left"
                else:
                    right_hand = hand_landmarks
                    right_label = "Right"
            
            # ส่งคำสั่งไปยังหุ่นยนต์
            angles = calculate_angles(left_hand, right_hand, left_label, right_label)
            arm.send_angles(angles)
        
        # แสดงคำแนะนำและค่ามุมปัจจุบัน
        guide = [
            f"Base: {arm.current_angles[0]} (4+ fingers left - X axis)",
            f"Gripper: {'close' if arm.current_angles[1] == 0 else 'open'} (<=1 finger right)",
            f"Tilt: {arm.current_angles[2]} (4+ fingers right - Y axis)",
            f"Pan: {arm.current_angles[3]} (3 fingers left - Y axis)"
        ]
        
        for i, text in enumerate(guide):
            y_pos = 30 + i * 25
            cv2.putText(image, text, (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        cv2.imshow('Robot Arm Hand Control', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

finally:
    arm.close()
    cap.release()
    cv2.destroyAllWindows()