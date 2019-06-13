import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
from googlesearch import search
import os
import smtplib
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" how can I help you")
    speak("There are lots of thing i can help u with for example")
    speak("send mail to a contact")
    speak("browse the internet")
    speak("play songs")
    speak("and many more,")
    speak("what would you like me to do?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source, duration=10)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Sorry couldn't get you, try again please")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    print("Voice Model initalizing")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("No such result found. Try again please")
        elif 'google' in query:
            speak('Searching google...')
            try:
                query = query.replace("google", "")
                num_page = 3
                search_results = search(query, num_page)
                for result in search_results:
                    print(result.description)
            except:
                speak("No such result found.Try again please")
        elif 'open youtube' in query:
            speak("opening youtube in your default browser")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google in your default browser")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("opening facebook in your default browser")
            webbrowser.open("facebook.com")   


        elif 'play music' in query:
            try:
                music_dir = 'D:\\songs\\Favorite Songs2'#file path which contains the music file
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            except:
                speak("There is some error with the path"  )

        elif 'the time' in query:
            T = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {T}")
        elif "how are you" in query:
            speak("I am fine")
        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on mate, I will show you where " + location + " is.")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
        elif 'shutdown' in query:
            sys.exit(speak("It was pleasure helping you"))

       