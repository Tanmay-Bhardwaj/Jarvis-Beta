#Importing Modules
from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
import os
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser as wb
import datetime
import pywhatkit


def speech_setup():
    global listener,engine,voice
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

speech_setup()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    global command
    global source
    try:
        with sr.Microphone() as source:
            global command
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

#Performing Tasks----------------------------------------------------------------------------------------------------------
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    talk("the current time is")
    talk(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    talk("the current date is")
    talk(f"{day},{month},{year}")
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    talk("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        talk("Good Morning!!")
        print("Good Morning!!")
    elif hour >= 12 and hour < 16:
        talk("Good Afternoon!!")
        print("Good Afternoon!!")
    elif hour >= 16 and hour < 24:
        talk("Good Evening!!")
        print("Good Evening!!")
    else:
        talk("Good Night Sir, See You Tommorrow")

def screenshot():
    global img_name
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Users\\Tanmay Bhardwaj\\OneDrive\\Tanmay\\Python\\Jarvis(data)\\ss.png")
    img.save(img_path)
    #talk("By what name should I save the screenshot")
    #with sr.Microphone() as source:
        #voice=listener.listen(source)
        #img_name=listener.recognize_google(voice)
        #img_name=command.lower()
        
def introduction():
    talk("I am Jarvis. A virtual, artificial intelligence and I am here to assist you in variety of tasks, as best as I can. twentyfour hours a day, and seven days a week. Importing all preferances from Home interface. Systems, now fully operational.")

def opening_websites():
        global site_to_be_opened
        site_to_be_opened=command.replace("open","")
        talk('Opening'+ site_to_be_opened)
        wb.open_new_tab(f"{site_to_be_opened}")

def playing_videos():
    video = command.replace('play',command)
    talk('playing ' + video)
    pywhatkit.playonyt(video)

def latest_news():
    talk("Showing the latest news ")
    newslink='https://www.bbc.com/news'
    wb.open_new_tab(newslink)

#-------------------------------------------------------------------------------------------------------------------------

def Jarvis():
    if __name__ == "__main__":
        wishme()
        while True:
            input('Press Enter to activate')
            
            #Loop for commands-----------------------------------------------------------------------------------------------------
            take_command()
            if "what is the time" in command:
                time()
            elif "what"and"date" and "today" in command:
                date()
            elif "take a screenshot" in command:
                screenshot()
            elif "open" in command:
                opening_websites()
            elif "play" in command:
                playing_videos()
            elif "show" and "latest" and "news" in command:
                latest_news()
            #Opening my own website('special')
            elif 'my website' in command:
                wb.open_new_tab("tanmaybhardwaj.in")

            else:
                print(command)
                llm=Ollama(model="llama3",request_timeout=12000.0)
                result=llm.complete(command)
                print(result)
                talk(result)
            #-------------------------------------------------------------------------------------------------------------------------

    
Jarvis()