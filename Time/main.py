import pyttsx3
import schedule

engine = pyttsx3.init()

def wake_up():
    engine.say("Hey, Wake up! Wake up! wake up!")
    engine.runAndWait()
input = input("Enter the time you want to wake up: ")
schedule.every().day.at(input).do(wake_up)

while 1:
    schedule.run_pending()