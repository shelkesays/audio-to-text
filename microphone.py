import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Start Talking")
    audio = r.listen(source)
    print("Stop Talkng")


try:
    txt = r.recognize_google(audio, language = "mr-IN")
except:
    pass

print(txt)
