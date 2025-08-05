import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
import pygame
import time
import musicLibrary
import requests
import API
import random

recognizer = sr.Recognizer()

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except Exception as e:
        print("Speech error:", e)

newsAPI_KEY = API.API_KEYS["newsKey"]

def processCommand(c):
    c = c.lower()
    if "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open google" in c:
        webbrowser.open("https://google.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open github" in c:
        webbrowser.open("https://github.com/")
    elif "play" in c:
        song = c.split("play", 1)[1].strip()
        link = musicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "news" in c:
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsAPI_KEY}")
        if res.status_code == 200:
            data = res.json()
            articles = data.get("articles", [])
            speak("Here are the latest news headlines.")
            for article in articles[:5]:
                title = article.get("title", "No Title")
                print("News:", title)
                speak(title)
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    elif any(word in c for word in ["exit", "shutdown", "quit", "stop"]):
        speak("Shutting down. Have a great day!")
        exit()


greetings = [
    "Hello, I'm Alexa, your virtual assistant. How can I brighten your day?",
    "Welcome back! Ready to assist.",
    "Hi there! What can I help you with today?",
    "Assistant online and ready to roll.",
]

responses = [
    "At your service!",
    "How can I assist you?",
    "I'm listening.",
    "Yes, what can I do for you?"
]

if __name__ == "__main__":
    speak(random.choice(greetings))
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio).lower()
                print("Heard:", word)
                if "alexa" in word:
                    speak(random.choice(responses))
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except Exception as e:
            print("Error:", e)
