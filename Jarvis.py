import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!, Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!, Sir")

    else:
        speak("Good Evening!!, Sir")

    speak("Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender\'s gmail id', 'your password')
    server.sendmail('sender\'s gmail id', to , content)
    server.close()

if __name__ == '__main__':
     # wishMe()
     while True:
         query = takeCommand().lower()
         #Logic for executing tasks based on query
         if 'wikipedia' in query:
             speak('Searching wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("Sir, According to wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open instagram' in query:
             webbrowser.open("instagram.com")

         elif 'open amazon' in query:
             webbrowser.open("amazon.in")

         elif 'quit' in query:
             speak("Bye Sir")
             quit()

         elif 'open google' in query:
             webbrowser.open("google.com")

         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")


         elif 'play music' in query:
             music_dir = 'E:\\lokesh\\Music'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, the time is {strTime}")

         elif 'open vs codes' in query:
             code_path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(code_path)

         elif 'open whatsapp' in query:
             whatsapp_path = "C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
             os.startfile(whatsapp_path)

         elif 'open spotify' in query:
             spotify_path = "C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe"
             os.startfile(spotify_path)

         elif 'send mail to Lokesh' in query:
             try:
                 speak("What should I say")
                 content = takeCommand()
                 to = "receiver's gmail id"
                 sendEmail(to,content)
                 speak("Email has been sent!! sir")
             except Exception as e:
                 print(e)
                 speak("Sorry sir, I am unable to send the email right now.")

         elif 'hello jarvis' in query:
             hour = int(datetime.datetime.now().hour)
             speak("Hello Sir, how are you?")
             if hour >= 8 and hour < 12:
                 speak("Good Morning!!! Sir")

             elif hour >=12 and hour < 18:
                 speak("Good afternoon!!! sir")

             else:
                 speak("Good Evening!!! Sir")

         elif 'who are you' in query:
             speak("I'm Jarvis, your personal assistant sir")

