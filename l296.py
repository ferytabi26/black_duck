import RPi.GPIO as GPIO
in1 = 13
in2 = 16
in3 = 18
in4 = 37
en1 = 32
en2 = 33
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

p1 = GPIO.PWM(en1,1000)
p2 = GPIO.PWM(en2,1000)
p1.start(0)
p2.start(0)
try:
    while True:
        #mundur
#         GPIO.output(in1,0)
#         GPIO.output(in2,1)
#         GPIO.output(in3,1)
#         GPIO.output(in4,0)
        #maju
#         GPIO.output(in1,1)
#         GPIO.output(in2,0)
#         GPIO.output(in3,0)
#         GPIO.output(in4,1)
        #kiri
#         GPIO.output(in1,1)
#         GPIO.output(in2,0)
#         GPIO.output(in3,1)
#         GPIO.output(in4,0)
        #kanan
#         GPIO.output(in1,1)
#         GPIO.output(in2,0)
#         GPIO.output(in3,1)
#         GPIO.output(in4,0)
#         p1.ChangeDutyCycle(35)
#         p2.ChangeDutyCycle(25)
        GPIO.output(in1,0)
        GPIO.output(in2,1)
        GPIO.output(in3,0)
        GPIO.output(in4,1)
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(40)
#         
#         
except keyboardinterrupt:
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    GPIO.cleanup()

