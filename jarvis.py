import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import time

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            return r.recognize_google(audio).lower()
        except sr.UnknownValueError:
             # Don't print error for silence/background noise
            return ""
        except Exception as e:
            print(e)
            return ""


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

def tell_time():
    speak(datetime.datetime.now().strftime("The time is %I:%M %p"))

def tell_date():
    speak(datetime.datetime.now().strftime("Today's date is %B %d, %Y"))


def wiki_search(topic):
    try:
        speak(wikipedia.summary(topic, sentences=2))
    except:
        speak("I found no results for that.")


def main():
    wish_me()
    speak("Say Jarvis to activate me")

    while True:
        command = listen()

        if not command:
            continue

        if "jarvis" in command:
            speak("Yes?")
            command = listen()

            if not command:
                speak("I didn't hear anything.")
                continue

            print(f"Command: {command}")


            if "time" in command:
                tell_time()

            elif "date" in command:
                tell_date()

            elif "wikipedia" in command:
                speak("What should I search?")
                topic = listen()
                if topic:
                    wiki_search(topic)

            elif "exit" in command or "stop" in command:
                speak("Goodbye")
                break

            else:
                speak("I did not understand")


if __name__ == "__main__":
    main()
