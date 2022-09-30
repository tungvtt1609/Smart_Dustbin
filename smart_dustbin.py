import telepot
import RPi.GPIO as GPIO
import time
from telepot.loop import MessageLoop
GPIO.setmode(GPIO.BCM)

PIN_TRIGGER = 18
PIN_ECHO = 17

print("Distance Measurement in Process")
GPIO.setup(PIN_TRIGGER, GPIO.OUT)


