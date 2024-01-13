import speech_recognition as sr 
import datetime
import pyttsx3
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<15:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvo! How can I assist you today?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google_cloud(audio,language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        print("Could you please say that again?")
        return "None"
    return query

if __name__=="__main__":
    greet()
    while True:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,lines=2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
    
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It's {time}")

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'quit' in query:
            speak("Thank you! Have a grat day!")
            exit()        
            






