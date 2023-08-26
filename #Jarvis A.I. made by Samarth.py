#Jarvis A.I. made by Samarth
import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#Jarvis A.I. made by Samarth
def generate_ran_password(length):
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_~-=+:;'<>,./?"
    password=" "
    for i in range(length):
        password+=random.choice(characters)
    return password

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis your own A.I. personal voice assistant. Please tell me how may I help you?")

def take_command():

#It takes microphone input from the user and returns the output in string form
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing.........")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        #speak("Please say that again couldn't hear you properly ")
        print("Please say that again")
        return "None"
    return query


#def send_email(to,content):
    #server=smptlib.SMPT('smntp.gmail.com',587)

if __name__=='__main__':
#speak("Hi! I am Jarvis A.I. developed by Samarth")
    wish_me()

    while True:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'jarvis open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Yes Sir opening Youtube")

        elif 'jarvis open google' in query:
            webbrowser.open("google.com")
            speak("Yes Sir opening Google")

        elif 'jarvis open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Yes Sir opening Gmail")

        elif 'jarvis open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("Yes Sir opening Instagram")

        elif 'jarvis open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Yes Sir opening Whatsapp")

        #elif 'open cmd' in query:
            #webbrowser.open("%windir%\\system32\\cmd.exe")

        elif 'jarvis open drive' in query:
            webbrowser.open("https://drive.google.com/drive/my-drive")
            speak("Yes Sir opening Google Drive")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")
            speak("Yes Sir opening Spotify")

        elif 'jarvis open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")
            speak("Yes Sir opening Linkedin")

        #elif 'open chat GPT' in query:
            #webbrowser.open("https://chat.openai.com/")

        elif 'jarvis open coursera' in query:
            webbrowser.open("https://www.coursera.org/")

        #elif 'open AI' in query:
            #webbrowser.open("https://bard.google.com/")

        elif 'jarvis open classroom' in query:
            webbrowser.open("https://classroom.google.com/")
            speak("Yes Sir opening Google Classroom")

        elif 'jarvis open chrome' in query:
            code_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_path)
            speak("Yes Sir opening Google Chrome")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'jarvis open vs code' in query:
            code_path = "C:\\Users\\HP\\Downloads\\HP Downloads\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Yes Sir opening VS code")

        elif 'jarvis open pycharm' in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.4\\bin\\pycharm64.exe"
            os.startfile(code_path)
            speak("Yes Sir opening Pycharm")

        elif 'jarvis who are you' in query:
            speak("I am Jarvis A.I. a personal voice assistant developed by Samarth")

        elif 'jarvis open zoom' in query:
            code_path = "C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(code_path)
            speak("Yes Sir opening Zoom Video Confrencing")

        elif 'jarvis generate a random password' in query:
            if __name__ == "__main__":
                password = generate_ran_password(14)
                print("The length of the password is:", len(password))
                print("Your randomly generated password is:", password)
                speak("Your password has been generated")


        #elif 'email to samarth' in query:
            #try:
                #speak("What should I write in the email. Sir?")
                #content = take_command()
                #to = "samarthguha8@gmail.com"
                #send_email(to,content)
                #speak("Sir the email has been sent!")
            #except Exception as e:
                #print(e)
                #speak("Sorry the email could not be sent")


#Jarvis A.I. made by Samarth
