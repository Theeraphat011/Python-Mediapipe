# Robotic Arm Hand Gesture Control System

A computer vision-based system that allows controlling a robotic arm using hand gestures captured through a webcam. The system uses MediaPipe for hand tracking and sends commands to an ESP32-controlled robotic arm.

![Project Demo](/image.png)

## Features

- Real-time hand tracking using MediaPipe
- Intuitive gesture control system for robotic arm manipulation
- Control multiple arm functions simultaneously with both hands
- Visual feedback with gesture detection display

## Hardware Requirements

- ESP32 development board
- Servo motors (4x)
  - Base servo (0-180°)
  - Keeper/gripper servo (0-8°)
  - Tilt servo (35-120°)
  - Pan servo (0-60°)
- Webcam
- Robot arm assembly
- USB cables
- Power supply for servos

## Software Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE
- ESP32 board support for Arduino

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Python-Mediapipe.git
   cd Python-Mediapipe
   ```

2. Install required Python packages:
   ```
   pip install opencv-python mediapipe pyserial numpy
   ```

3. Install Arduino IDE and ESP32 board support
   - Follow instructions at https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html

4. Connect the ESP32 and upload the Arduino code:
   - Open Arduino IDE
   - Open `Arduino/main.ino` 
   - Select your ESP32 board and COM port
   - Upload the sketch

5. Wire the servo motors to the ESP32 according to the pin definitions in the Arduino code:
   - Base servo: GPIO 26
   - Keeper servo: GPIO 25
   - Tilt servo: GPIO 33
   - Pan servo: GPIO 32

## Usage

1. Connect the ESP32 to your computer via USB
2. Run the Python script:
   ```
   python main.py
   ```
3. Position yourself in front of the webcam
4. Use hand gestures to control the robot arm:

### Control Scheme

**Left Hand:**
- 4+ fingers extended: Control base rotation (X-axis movement)
- 3 fingers extended: Control pan (Y-axis movement)

**Right Hand:**
- 0-1 fingers extended: Close gripper
- 2+ fingers extended: Open gripper
- All gestures: Control tilt based on hand height (Y-axis)

## How It Works

The system uses MediaPipe's hand tracking capabilities to detect hand landmarks in the webcam feed. These landmarks are processed to determine finger positions and gestures. Based on the detected gestures and hand positions, control signals are sent via serial communication to the ESP32, which then controls the servo motors on the robotic arm.

The Python script includes:
- Hand detection and landmark tracking
- Finger counting algorithm
- Position-to-angle mapping
- Serial communication with ESP32

The ESP32 code handles:
- Servo control
- Serial communication with the Python script
- Angle constraints and safety limits

## Customization

You can customize the control scheme by modifying the `calculate_angles()` function in `main.py`. Servo limits and pin assignments can be adjusted in the Arduino code.

## Troubleshooting

- **Serial Connection Issues**: Ensure the correct COM port is specified in `main.py`
- **Gesture Recognition Problems**: Adjust the detection and tracking confidence thresholds
- **Servo Movement Issues**: Check power supply and ensure servo limits are properly set
- **Calibration Issues**: You may need to adjust the angle ranges in both Python and Arduino code based on your specific robotic arm model

## Project Gallery

### Setup Software and Hardware
<div align="center">
  <img src="/image4.png" alt="Hardware Setup" width="45%">
  <img src="/image5.png" alt="Hardware Setup" width="45%">
</div>
<div align="center">
  <img src="/image6.png" alt="Hardware Setup" width="30%">
  <img src="/image7.png" alt="Hardware Setup" width="30%">
  <img src="/image3.png" alt="Hardware Setup" width="30%">
</div>
<p align="center"><em>The complete robotic arm setup with ESP32 and servos</em></p>

### Hand Gesture Detection
<div align="center">
  <img src="/image1.png" alt="Hand Detection" width="80%">
</div>
<p align="center"><em>MediaPipe hand tracking in action showing finger detection</em></p>

### Demonstration
<div align="center">
  <img src="/image2.png" alt="Project Demo" width="80%">
</div>
<p align="center"><em>Controlling the robotic arm with hand gestures</em></p>

## Future Improvements

- Add voice control capabilities
- Implement preset gestures for common movements
- Create mobile app interface for additional control options
- Add machine learning for gesture personalization
- Improve motion smoothing algorithms

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe team for their hand tracking solution
- ESP32 and Arduino communities
- OpenCV community for computer vision tools
- Contributors and testers who helped refine this project

---

# ระบบควบคุมแขนกลด้วยท่าทางมือ

ระบบคอมพิวเตอร์วิชันที่ช่วยให้สามารถควบคุมแขนกลด้วยท่าทางมือผ่านเว็บแคม ระบบนี้ใช้ MediaPipe สำหรับการติดตามมือและส่งคำสั่งไปยังแขนกลที่ควบคุมด้วย ESP32

![การสาธิตโครงงาน](/image.png)

## คุณสมบัติ

- การติดตามมือแบบเรียลไทม์ด้วย MediaPipe
- ระบบควบคุมด้วยท่าทางที่ใช้งานง่าย
- ควบคุมฟังก์ชันหลายอย่างของแขนกลพร้อมกันด้วยทั้งสองมือ
- แสดงผลการตรวจจับท่าทางแบบมีภาพประกอบ

## อุปกรณ์ที่ต้องการ

- บอร์ด ESP32
- เซอร์โวมอเตอร์ (4 ตัว)
  - เซอร์โวฐาน (0-180°)
  - เซอร์โวคีปเปอร์/กริปเปอร์ (0-8°)
  - เซอร์โวเอียง (35-120°)
  - เซอร์โวหัน (0-60°)
- เว็บแคม
- ชุดประกอบแขนกล
- สาย USB
- แหล่งจ่ายไฟสำหรับเซอร์โว

## ซอฟต์แวร์ที่ต้องการ

- Python 3.6+
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE
- ESP32 board support สำหรับ Arduino

## การติดตั้ง

1. โคลนโปรเจคนี้:
   ```
   git clone https://github.com/yourusername/Python-Mediapipe.git
   cd Python-Mediapipe
   ```

2. ติดตั้งแพคเกจ Python ที่จำเป็น:
   ```
   pip install opencv-python mediapipe pyserial numpy
   ```

3. ติดตั้ง Arduino IDE และ ESP32 board support
   - ทำตามคำแนะนำที่ https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html

4. เชื่อมต่อ ESP32 และอัปโหลดโค้ด Arduino:
   - เปิด Arduino IDE
   - เปิดไฟล์ `Arduino/main.ino` 
   - เลือกบอร์ด ESP32 และพอร์ต COM
   - อัปโหลดโค้ด

5. เดินสายเซอร์โวมอเตอร์ไปยัง ESP32 ตามการกำหนดค่าพินในโค้ด Arduino:
   - เซอร์โวฐาน: GPIO 26
   - เซอร์โวคีปเปอร์: GPIO 25
   - เซอร์โวเอียง: GPIO 33
   - เซอร์โวหัน: GPIO 32

## การใช้งาน

1. เชื่อมต่อ ESP32 กับคอมพิวเตอร์ผ่าน USB
2. รันสคริปต์ Python:
   ```
   python main.py
   ```
3. จัดตำแหน่งตัวเองให้อยู่หน้าเว็บแคม
4. ใช้ท่าทางมือเพื่อควบคุมแขนกล:

### วิธีการควบคุม

**มือซ้าย:**
- ชูนิ้ว 4 นิ้วขึ้นไป: ควบคุมการหมุนฐาน (การเคลื่อนที่แกน X)
- ชูนิ้ว 3 นิ้ว: ควบคุมการหัน (การเคลื่อนที่แกน Y)

**มือขวา:**
- ชูนิ้ว 0-1 นิ้ว: ปิดกริปเปอร์
- ชูนิ้ว 2 นิ้วขึ้นไป: เปิดกริปเปอร์
- ทุกท่าทาง: ควบคุมการเอียงตามความสูงของมือ (แกน Y)

## การทำงานของระบบ

ระบบใช้ความสามารถในการติดตามมือของ MediaPipe เพื่อตรวจจับจุดสำคัญบนมือจากภาพเว็บแคม จุดเหล่านี้ถูกประมวลผลเพื่อระบุตำแหน่งและท่าทางของนิ้วมือ จากท่าทางและตำแหน่งของมือที่ตรวจจับได้ สัญญาณควบคุมจะถูกส่งผ่านการสื่อสารแบบอนุกรมไปยัง ESP32 ซึ่งจะควบคุมเซอร์โวมอเตอร์บนแขนกล

สคริปต์ Python ประกอบด้วย:
- การตรวจจับมือและการติดตามจุดสำคัญ
- อัลกอริทึมนับนิ้วมือ
- การแปลงตำแหน่งเป็นมุม
- การสื่อสารแบบอนุกรมกับ ESP32

โค้ด ESP32 จัดการเรื่อง:
- การควบคุมเซอร์โว
- การสื่อสารแบบอนุกรมกับสคริปต์ Python
- ข้อจำกัดของมุมและความปลอดภัย

## การปรับแต่ง

คุณสามารถปรับแต่งรูปแบบการควบคุมได้โดยแก้ไขฟังก์ชัน `calculate_angles()` ใน `main.py` สามารถปรับขีดจำกัดของเซอร์โวและการกำหนดพินได้ในโค้ด Arduino

## การแก้ไขปัญหา

- **ปัญหาการเชื่อมต่อแบบอนุกรม**: ตรวจสอบให้แน่ใจว่าระบุพอร์ต COM ที่ถูกต้องใน `main.py`
- **ปัญหาการรู้จำท่าทาง**: ปรับค่าความเชื่อมั่นในการตรวจจับและติดตาม
- **ปัญหาการเคลื่อนไหวของเซอร์โว**: ตรวจสอบแหล่งจ่ายไฟและตรวจสอบให้แน่ใจว่าขีดจำกัดของเซอร์โวถูกตั้งค่าอย่างเหมาะสม
- **ปัญหาการสอบเทียบ**: คุณอาจต้องปรับช่วงมุมทั้งในโค้ด Python และ Arduino ตามรุ่นของแขนกลที่ใช้

## แกลเลอรีโครงงาน

### การเซ็ตอัพซอฟต์แวร์และฮาร์ดแวร์
<div align="center">
  <img src="/image4.png" alt="การเซ็ตอัพฮาร์ดแวร์" width="45%">
  <img src="/image5.png" alt="การเซ็ตอัพฮาร์ดแวร์" width="45%">
</div>
<div align="center">
  <img src="/image6.png" alt="การเซ็ตอัพฮาร์ดแวร์" width="30%">
  <img src="/image7.png" alt="การเซ็ตอัพฮาร์ดแวร์" width="30%">
  <img src="/image3.png" alt="การเซ็ตอัพฮาร์ดแวร์" width="30%">
</div>
<p align="center"><em>การติดตั้งแขนกลสมบูรณ์พร้อม ESP32 และเซอร์โว</em></p>

### การตรวจจับท่าทางมือ
<div align="center">
  <img src="/image1.png" alt="การตรวจจับมือ" width="80%">
</div>
<p align="center"><em>การติดตามมือของ MediaPipe แสดงการตรวจจับนิ้วมือ</em></p>

### การสาธิต
<div align="center">
  <img src="/image2.png" alt="การสาธิตโครงงาน" width="80%">
</div>
<p align="center"><em>การควบคุมแขนกลด้วยท่าทางมือ</em></p>

## การพัฒนาในอนาคต

- เพิ่มความสามารถในการควบคุมด้วยเสียง
- รองรับท่าทางที่กำหนดไว้ล่วงหน้าสำหรับการเคลื่อนไหวทั่วไป
- สร้างอินเทอร์เฟซแอปพลิเคชันมือถือสำหรับตัวเลือกการควบคุมเพิ่มเติม
- เพิ่มการเรียนรู้ของเครื่องสำหรับการปรับแต่งท่าทางส่วนบุคคล
- ปรับปรุงอัลกอริทึมการทำให้การเคลื่อนไหวนุ่มนวลขึ้น

