import telepot
import RPi.GPIO as GPIO
import time
from telepot.loop import MessageLoop
GPIO.setmode(GPIO.BCM)

PIN_TRIGGER = 18
PIN_ECHO = 17

print("Distance Measurement in Process")
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.setwarnings(False)
GPIO.output(PIN_TRIGGER, False)
print("Waiting for sensor to Settle")
time.sleep(2)

globalMessageNew = 0
globalMessage = 0



#function for sending message

def sendMessage(globalMessage):
    global telegramText
    global chat_id
    global showMessage

    if globalMessage == 1:
        bot.sendMessage(chat_id, "FULL!!!")
    elif globalMessage == 2:
        bot.sendMessage(chat_id, "WARNING!!!")
    elif globalMessage == 3:
        bot.sendMessage(chat_id, "LOW!!!")

def mainprogram():
    GPIO.output(PIN_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, False)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(PIN_ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    global distance
    distance = pulse_duration * 17150
    distance = round(distance)

    global chat_id
    global globalMessage
    global globalMessageNew
    print("Distance: ", distance)

    if distance <= 5:
        globalMessage = 1
        if globalMessageNew != globalMessage:
            sendMessage(globalMessage)
            globalMessageNew = globalMessage
        else:
            globalMessageNew = globalMessage

    elif distance <= 10 and distance > 5:
        globalMessage = 2
        if globalMessageNew != globalMessage:
            sendMessage(globalMessage)
            globalMessageNew = globalMessage
        else:
            globalMessageNew = globalMessage
    elif distance <= 21 and distance > 10:
        globalMessage = 3
        if globalMessageNew != globalMessage:
            sendMessage(globalMessage)
            globalMessageNew = globalMessage
        else:
            globalMessageNew = globalMessage

    time.sleep(10)

def handle(msg):
    global telegramText
    global chat_id
    global showMessage
    global distance

    chat_id = msg["chat"]["id"]
    telegramText = msg["text"]

    print("Message received from " + str(chat_id))
    if telegramText == "/start":
        bot.sendMessage(chat_id, "Welcome to smart dustbin")
        bot.sendMessage(chat_id, "Location: ")

        while True:
            mainprogram()

bot = telepot.Bot('779066943:AAGMLfHzwiyWro1nmMCfe_kTrkd8zOZc2i8')
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)


