from gtts import gTTS

language = "bn"
# text = "Hello, This is Ameer This is my first test of text to voice"
text = "যুক্তরাষ্ট্রের এই উদ্যোগে ফিলিস্তিন সমস্যা গৌণ হয়ে যাবে। তবে এ জন্য যুক্তরাষ্ট্রকে চড়া মূল্যও দিতে হতে পারে।"

speech = gTTS(text = text, lang = language, slow = False  )
# speech.save("txtToSpeech.mp3")
speech.save("txtToSpeechBangla2.mp3")