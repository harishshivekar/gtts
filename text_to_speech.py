import gtts
import playsound
import os


def speaker():
    convert = gtts.gTTS(text, lang="en")

    convert.save("speak.mp3")

    playsound.playsound("speak.mp3")

    os.remove("speak.mp3")


def shutting_down():
    say = "Bye Bye I am go to shut down"
    co2 = gtts.gTTS(text=say, lang="en")
    co2.save("temp.mp3")
    playsound.playsound("temp.mp3")
    os.remove("temp.mp3")


while True:
    text = input("Enter the words: ")

    if text == "shut down":
        print("Bye Bye I am going to shut down")
        shutting_down()
        break

    speaker()
