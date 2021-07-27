# voice recognition packages
import speech_recognition as sr
import os
import random
import pyttsx3
import playsound
from tkinter import *
from threading import *
import time
import subprocess
import webbrowser
import geocoder
import pywhatkit
import wikipedia
import datetime
import pyautogui
from tkinter import messagebox


def voice_assistant():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def there_exists(terms):
        for term in terms:
            if term in voice_data:
                return True

    def speak(audio_string):
        engine.say(audio_string)
        engine.runAndWait()

    def record_audio():
        with sr.Microphone() as source:

            audio = r.listen(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                text.insert(INSERT, "\nSorry, I cant understand")
                speak('Sorry, I cant understand')

            except sr.RequestError:
                text.insert(INSERT, "\nPlease try again")
                speak('Please try again')

            return voice_data

    def note(text):
        dateandtime = datetime.datetime.now().strftime('%d-%m-%Y  %I:%M:%S %p').replace(':', '_')
        file_name = f'notes/{dateandtime} -note.txt'
        with open(file_name, "w") as f:
            f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

    def respond(voice_data):

        if there_exists(["what's your name", 'what is your name', 'tell me your name', 'your name']):
            text.insert(INSERT, "\nI am MIKASA")
            speak('I am MIKASA')
            pass

        elif there_exists(['open this PC', 'open my computer']):
            text.insert(INSERT, "\nOpening This PC")
            speak('Opening This PC')
            os.system('explorer =')
            pass

        elif there_exists(['create a text file', 'text file', 'create a new text document', 'create a text document']):
            desktop = os.path.expanduser("~\Desktop")
            file = open(f"{desktop}/New Text Document.txt", "w")
            file.write("Created by MIKASA")
            file.close()
            text.insert(INSERT, "\nA text file is created on the Desktop")
            speak('A text file is created on the Desktop')
            pass

        elif there_exists(['make a note', 'remember this']):
            speak("What would you like me to write down?")
            note_text = record_audio()
            note(note_text)
            speak("I've made a note of that.")

        elif 'play' in voice_data:
            data = voice_data.replace('play', '')
            text.insert(INSERT, "\n"+f'playing {data} on YouTube')
            speak(f'playing {data} on YouTube')
            pywhatkit.playonyt(data)
            pass

        elif there_exists(["what is the time", "what's the time", "tell me the time", "what time is it"]):
            time = datetime.datetime.now().strftime('%I:%M %p')
            text.insert(INSERT, "\n"+time)
            speak('Current time is ' + time)
            pass

        elif there_exists(['What is', 'what is']):
            search_term = voice_data.split("is")[-1]
            info = wikipedia.summary(search_term, 1)
            text.insert(INSERT, "\nAccording to Wikipedia, "+info)
            speak('According to Wikipedia, ' + info)
            pass

        elif there_exists(["search for"]):
            search_term = voice_data.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            text.insert(INSERT, "\n"+f'Here is what I found for {search_term} on google')
            speak(f'Here is what I found for {search_term} on google')
            pass

        elif there_exists(["on YouTube"]):
            search_term = voice_data.split("on")[0]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            text.insert(INSERT, "\n"+f'Here is what I found for {search_term} on youtube')
            speak(f'Here is what I found for {search_term} on youtube')
            pass

        elif there_exists(["how are you", "how are you doing"]):
            text.insert(INSERT, "\n"+"I'm very well, thanks for asking")
            speak("I'm very well, thanks for asking")
            pass

        elif there_exists(["where am I"]):
            g = geocoder.ip('me')
            text.insert(INSERT, "\nYou're approximately  somewhere around " + g.city)
            speak("You're approximately  somewhere around " + g.city)
            # url = "https://www.google.com/maps/search/my+location/"
            # webbrowser.get().open(url)
            # speak("You must be somewhere near here, as per Google maps")
            pass

        elif there_exists(["toss", "flip", "coin", 'flip a coin', 'Toss a Coin']):
            moves = ["heads", "tails"]
            playsound.playsound('sfx/cointoss_sfx.mp3')
            cmove = random.choice(moves)
            text.insert(INSERT, "\nYou got " + cmove)
            speak("You got " + cmove)

        elif there_exists(['help', 'Help']):
            '''open a list of commands on a new window'''
            listofcommands()
            pass

        elif there_exists(["screenshot", "take a screenshot", "snapshot"]):
            pyautogui.hotkey('win', 'printscreen')
            text.insert(INSERT, "\nScreenshot is saved in the default location")
            speak("Screenshot is saved in the default location")
            pass

        elif there_exists(["open local disk"]):
            data = voice_data.replace('open local disk', '')
            text.insert(INSERT, "\n"+f"Opening Local Disk {data}")
            speak(f"Opening Local Disk {data}")
            os.system(f'explorer {data}:')
            pass

        elif there_exists(["screenshot", "take a screenshot", "snapshot", "take a snapshot"]):
            pyautogui.hotkey('win', 'printscreen')
            text.insert(INSERT, "\nScreenshot is saved in the default location")
            speak("Screenshot is saved in the default location")
            pass

        elif there_exists(['sleep']):
            text.insert(INSERT, '\nYour System will fall asleep shortly')
            speak("Your System will fall asleep shortly")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            pass

        elif there_exists(['shutdown', "shutdown the computer", "shutdown the PC"]):
            text.insert(INSERT, "\nTurning Off the PC")
            speak("Turning Off the PC")
            os.system("Shutdown.exe -s -t 00")
            pass

        elif there_exists(['restart', "restart the computer", "restart the PC"]):
            text.insert(INSERT, "\nRestarting the Computer")
            speak('Restarting the Computer')
            os.system('Shutdown.exe -r -t 00')
            pass

        elif there_exists(['goodbye', 'stop']):
            text.insert(INSERT, "\nGoodbye")
            speak('Goodbye')
            button['text'] = 'Start'
            exit()
            pass

        else:
            text.insert(INSERT, "\nTry something else")
            speak("Try something else")
            pass

    text.insert(INSERT, "\nhi there, how can i help you?")
    speak('hi there, how can i help you?')

    while True:
        playsound.playsound('sfx/rec_sfx.mp3')
        voice_data = record_audio()
        if voice_data != '':
            def usedstring():
                text.insert(INSERT, "\n~ "+voice_data)
            thread3 = Thread(target=usedstring())
            thread3.start()
            respond(voice_data)
        else:
            pass


# button  change on click and function call
def change_button2():
    if button['text'] == 'Start':
        button['text'] = 'Stop'
        thread1 = Thread(target=voice_assistant)
        thread1.start()
    else:
        button['text'] = 'Start'
        time.sleep(20)


def change_button():
    thread0 = Thread(target=change_button2())
    thread0.start()

# ############### butons inside help menu bar  ###############################
def about():
    with open("help/about.txt") as f:
        readme = f.read()
        messagebox.showinfo(title="About", message=str(readme))

def listofcommands():
    with open("help/commandlist.txt") as f:
        readme = f.read()
        messagebox.showinfo(title="List of Commands", message=str(readme))
# ############################################################################

# gui window properties
tkWindow = Tk()
tkWindow.geometry('400x480')
tkWindow.title('MIKASA')
tkWindow.iconbitmap('mikasa.ico')
text = Text(tkWindow)
menubar = Menu(tkWindow)
text.pack()

# menu bar
file = Menu(menubar, tearoff=0)
file.add_command(label="Exit", command=tkWindow.quit)
menubar.add_cascade(label="File", menu=file)

help = Menu(menubar, tearoff=0)
help.add_command(label="List of Commands",  command=listofcommands)
help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help)

# gui button
button = Button(tkWindow, text='Start', command=change_button, width=15)
button.pack(side=BOTTOM, padx=0, pady= 20)

tkWindow.config(menu=menubar)
tkWindow.mainloop()
