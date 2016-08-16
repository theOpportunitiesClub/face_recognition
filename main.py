from gpiozero import LED, Button
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from ImageEncoder import FacialRecognition


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

button = Button(4)
camera = PiCamera()

def take_picture():
    camera.capture('/home/pi/Desktop/dummy.jpg')
    camera.stop_preview()
    

    #FacialRecognition
    kairos = FacialRecognition('/home/pi/Desktop/dummy.jpg')
    kairos.recognize_image('/home/pi/Desktop/dummy.jpg')
    

def main():
    i = GPIO.input(17)
    if i==0:
        usr_input = int(input("Object detected!! Live feed? (y=1/n=0)"))
        if usr_input == 1:
            camera.start_preview()
            #break
        elif usr_input == 0:
            print "Sorry for the inconvenience."
            GPIO.cleanup()
        else:
            print "Wrong input. Running the program again."
            main()
            


#show picture UI

while True:
    main()

button.when_pressed = take_picture   
        
