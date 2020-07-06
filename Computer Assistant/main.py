# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 01:41:47 2020

@author: HP
"""


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') # microsoft voice api
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!")
    else:
        speak("Good Evening !!")

    speak("I am your assistant sir !! how may I help you ?")

def takeCommand():
    ''' takes microphone input and return string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ... ... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising... ... ...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Please say that again .. .. ")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    if 1:
    #while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia. .. ..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hello!! The time is {strTime}")

        elif 'competitive programming template' in query:
            codePath = "C:\\Users\\HP\\Desktop\\submit.cpp"
            os.startfile(codePath)
