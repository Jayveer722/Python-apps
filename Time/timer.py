import time
import pyttsx3
 
input = input("Enter the time you want to set in timer: ")
time.sleep(1500)
def wake_up():
    engine = pyttsx3.init()
    engine.say("Hey, Time is up! Time is up! Time is up!")
    engine.runAndWait()
wake_up()