import pywhatkit
import datetime

def send_whatsapp():
    number = input("Enter phone number (with country code): ")
    message = input("Enter your message: ")

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Schedule 2 mins from now

    pywhatkit.sendwhatmsg(number, message, hour, minute)
    print("WhatsApp message scheduled!")
