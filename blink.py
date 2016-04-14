import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinNumLED = 23
pinNumBCM = 24
GPIO.setup(pinNumLED,GPIO.OUT)
GPIO.setup(pinNumBCM,GPIO.IN)

while True:

       if (GPIO.input(pinNumBCM)):
              GPIO.output(pinNumLED,GPIO.HIGH)

       else:
              GPIO.output(pinNumLED,GPIO.HIGH)
              time.sleep(1)
              GPIO.output(pinNumLED,GPIO.LOW)
              time.sleep(1)
       
GPIO.cleanup()



