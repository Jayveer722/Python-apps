import webbrowser
import schedule

def open_link(link):
    webbrowser.open(link)

input = input("Enter the link: ")

schedule.every().day.at("16:59").do(open_link, input)

while 1:
    schedule.run_pending()