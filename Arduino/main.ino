#include <ESP32Servo.h>

// กำหนดขา Servo
#define BASE_PIN 26
#define KEEPER_PIN 25
#define TILT_PIN 33
#define PAN_PIN 32

// กำหนดค่าเริ่มต้น
#define DEFAULT_BASE 90
#define DEFAULT_KEEPER 0
#define DEFAULT_TILT 110
#define DEFAULT_PAN 45เ

Servo baseServo;    // หมุนฐาน (0-180°)
Servo keeperServo;  // เปิด-ปิด gripper (0-8°)
Servo tiltServo;    // ก้ม-เงย (45-135°)
Servo panServo;     // หมุนข้อมือ (45-90°)

void setup() {
  Serial.begin(115200);
  
  // ติดตั้ง Servo
  baseServo.attach(BASE_PIN);
  keeperServo.attach(KEEPER_PIN);
  tiltServo.attach(TILT_PIN);
  panServo.attach(PAN_PIN);
  
  // ตั้งค่าเริ่มต้น
  baseServo.write(90);
  keeperServo.write(0);
  tiltServo.write(110);
  panServo.write(0);
  
  delay(1000); // รอให้ Servo ไปตำแหน่งเริ่มต้น
}

void loop() {
  if (Serial.available() >= 4) {
    // อ่านค่ามุมทั้ง 4 จาก Python (เรียงลำดับ base, keeper, tilt, pan)
    byte baseAngle = Serial.read();
    byte keeperAngle = Serial.read();
    byte tiltAngle = Serial.read();
    byte panAngle = Serial.read();
    
    // ตรวจสอบข้อจำกัดของมุม
    baseAngle = constrain(baseAngle, 0, 180);  // Base (0-180°)
    keeperAngle = constrain(keeperAngle, 0, 8); // Keeper (0-8°)
    tiltAngle = constrain(tiltAngle, 35, 120);  // Tilt (120-35°)
    panAngle = constrain(panAngle, 0, 60);      // Pan (0-60)
    
    // ควบคุม Servo
    baseServo.write(baseAngle);
    keeperServo.write(keeperAngle);
    tiltServo.write(tiltAngle);
    panServo.write(panAngle);
    
    // ส่งค่ากลับเพื่อตรวจสอบ (optional)
    Serial.print("Received: ");
    Serial.print(baseAngle); Serial.print(" ");
    Serial.print(keeperAngle); Serial.print(" ");
    Serial.print(tiltAngle); Serial.println(" ");
    Serial.println(panAngle);
  }
}