import speech_recognition as sr

r = sr.Recognizer()

record = sr.AudioFile("male.wav")
with record as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)

text = r.recognize_google(audio, language="en-US")

with open("male.txt", mode="w") as txt_file:
    txt_file.write(text)



