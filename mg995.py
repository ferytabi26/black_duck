import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
servoPIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN,50)
pwm.start(0)

def SetAngle(angle):
    duty = angle/18+2
    GPIO.output(servoPIN,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN,False)
    pwm.ChangeDutyCycle(0)
try:
    while True:
            SetAngle(45)
        
except Keyboardinterrupt:
    p.stop()
    GPIO.cleanup()