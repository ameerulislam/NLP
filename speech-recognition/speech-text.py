# from transformers import pipeline

# cls = pipeline("automatic-speech-recognition")

# res = cls("txtToSpeechBangla.mp3")

# print(res)


import speech_recognition as sr
r = sr.Recognizer()

bangla1 = sr.AudioFile('txtToSpeechBangla2.wav')

with bangla1 as source:
    audio = r.record(source)

print(r.recognize_google(audio,language = "bn-BN"))
