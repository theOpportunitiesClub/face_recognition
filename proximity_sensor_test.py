from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    i = GPIO.input(17)
    if i==0:
        print "Obstacle detected", i
        #sleep(0.1)
