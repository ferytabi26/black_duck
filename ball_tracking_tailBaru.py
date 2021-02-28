from collections import deque
import numpy as np
import imutils
import cv2
import RPi.GPIO as GPIO
from time import sleep

in1 = 13
in2 = 16
in3 = 18
in4 = 37
en1 = 32
en2 = 33
servoPIN = 31

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(servoPIN, GPIO.OUT)

p1 = GPIO.PWM(en1,1000)
p2 = GPIO.PWM(en2,1000)
pwm = GPIO.PWM(servoPIN,50)
p1.start(100)
p2.start(100)
pwm.start(0)

orangeLower = (0, 118, 79)
orangeUpper = (20, 251, 255)

camera = cv2.VideoCapture(0)
position = 90
positionx = 0
while True:
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=400)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        if x < 100:
            position += 1
            positionx = 1
        elif x > 400:
            position -= 1
            positionx = 2
        elif x>150 and x<450 and radius>80 and radius<180:
            positionx = 0
        elif radius < 80  and x>150 and x<450:
            positionx = 3
        elif radius > 180 and x>150 and x<450:
            positionx = 4
        print(radius)
    
    if position > 119:
        position = 120
    elif position < 1:
        position = 0
    
#     duty = position/18+2
#     GPIO.output(servoPIN,True)
#     pwm.ChangeDutyCycle(duty)
    
    if positionx == 1:
        GPIO.output(in1,1)
        GPIO.output(in2,0)
        GPIO.output(in3,1)
        GPIO.output(in4,0)
        p1.ChangeDutyCycle(30)
        p2.ChangeDutyCycle(30)
        
    elif positionx == 2:
        GPIO.output(in1,0)
        GPIO.output(in2,1)
        GPIO.output(in3,0)
        GPIO.output(in4,1)
        p1.ChangeDutyCycle(30)
        p2.ChangeDutyCycle(30)
        
    elif positionx == 3:
        GPIO.output(in1,1)
        GPIO.output(in2,0)
        GPIO.output(in3,0)
        GPIO.output(in4,1)
        p1.ChangeDutyCycle(30)
        p2.ChangeDutyCycle(30)
        
    elif positionx == 4:
        GPIO.output(in1,0)
        GPIO.output(in2,1)
        GPIO.output(in3,1)
        GPIO.output(in4,0)
        p1.ChangeDutyCycle(30)
        p2.ChangeDutyCycle(30)
        
    elif positionx == 0:
        GPIO.output(in1,0)
        GPIO.output(in2,0)
        GPIO.output(in3,0)
        GPIO.output(in4,0)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

