import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice",voices[0].id)

def vspeak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"Master said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Master please pardon...")   #Say that again will be printed in case of improper voice 
        return "Master please pardon..." #None string will be returned
    return query

def wishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
   vspeak("GoodMorning! Master")
  elif hour>=12 and hour<18:
   vspeak("Goodafternoon! Master")
  else:
      vspeak("Goodevening! Master")

  vspeak("I Am Arcnoid! What can i do for you master")
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your gmail",'password')
    server.sendmail("your email",to,content)
    server.close()

if __name__=="__main__":
    #vspeak("Rachit is best dude")
    wishMe()
    while True:
      query=takeCommand().lower()
      #login for task based on your speech
      if "wikipedia" in query or "who is" in query:
          vspeak("Master scanning for data...")
          query=query.replace("wikipedia","")
          query=query.replace("who is","")
          results=wikipedia.summary(query,sentences=3)
          vspeak("According to wikipedia...")
          vspeak(results)
      elif "open youtube" in query:
          vspeak("opening youtube for you my master")
          webbrowser.open('youtube.com')
      elif "open google" in query:
          vspeak("opening google for you my master")
          webbrowser.open('google.com')
      elif "play pitbull" in query:
           vspeak("Master playing pitbull songs from my data base")
           music_dir1="C:\\Users\\hp\\Music\\Playlists\\pitbull collection"
           songs= os.listdir(music_dir1)
           print(songs)
           os.startfile(os.path.join(music_dir1,songs[0]))
      elif "the time" in query:
              strTime= datetime.datetime.now().strftime("%H:%M:%S")
              vspeak(f"mater right now time is...{strTime}")
      elif "on youtube" in query:
              search_youtube=takeCommand()
              search_youtube=search_youtube.replace("play","")
              search_youtube=search_youtube.replace("on youtube","")
              vspeak("found this result you honor")
              pywhatkit.playonyt(search_youtube)
      elif "joke" in query or "jokes" in query:
              vspeak(pyjokes.get_joke(language='en', category='all'))
      elif "open zoom" in query:
              zoom_path= "C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
              os.startfile(zoom_path)
      '''elif "send a mail to mom":
          try:
              vspeak("What message should I send master")
              content=takeCommand()
              to="email id to whom you want to send"
              sendEmail(to,content)
              vspeak("Master email has been successfully delivered!")
          except Exception as e:
              print(e)
              vspeak("Sorry master! I am unable to deliver your message due to some technical issues") '''
