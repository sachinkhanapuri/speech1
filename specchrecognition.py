import speech_recognition as sr

r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    print("speak something:")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("the speak you {}".format(text))
    except:
        print("you speak is not recognition")

