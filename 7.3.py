import time
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

##DECLARATION
led = LED(11)
pwm_led = GPIO.PWM(11, 50)
pwm_led.start(100)

TRIG = 18
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)
GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

##THis method sets up the distance for ultrasonic sesnor
def distance():
    GPIO.output(TRIG, True)
    
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(ECHO)==0:
        StartTime = time.time()
    
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance =  TimeElapsed * 17150
    distance = round(distance,2)
    
    return distance

while True:
    dist = distance()
    brightnessLvl = int(dist)
    if (dist < 100):
        pwm_led.ChangeDutyCycle(brightnessLvl)
        time.sleep(0.5)
    ## Won't turn LED ON IF ITS TOO FAR
    
    
    
    