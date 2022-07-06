import datetime
def gatedate():
    return datetime.datetime.now()
import schedule
import time
def water():
        from pygame import mixer
        mixer.init()
        mixer.music.load("water.mp3.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        a = input("Sir/Mam please give me input as drank or not drank when you get notification regarding water drink\n")
        f = open("water drink record.txt", "a")
        f.write(str([str(gatedate())]) + ": " + a + "\n")
        if a=="drank":
                mixer.music.stop()
        else:
                print("You must be serious about your health")
                mixer.music.stop()

def eyes():
        from pygame import mixer
        mixer.init()
        mixer.music.load("eyes.mp3.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        b = input("Sir/Mam please give me input as eye done or eye not done when you get notification regarding eye exercise\n")
        f = open("eye exercise record.txt", "a")
        f.write(str([str(gatedate())]) + ": " + b + "\n")
        if b=="eye done":
                mixer.music.stop()
        else:
                print("You must be serious about your health")
                mixer.music.stop()

def py():
        from pygame import mixer
        mixer.init()
        mixer.music.load("physical.mp3.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        c = input(" Sir/Mam please give me input as PE done or PE not done when you get notification regarding physical exercise\n")
        f = open("physical exercise record.txt", "a")
        f.write(str([str(gatedate())]) + ": " + c + "\n")
        if c=="PE done":
                mixer.music.stop()
        else:
                print("You must be serious about your health")
                mixer.music.stop()

schedule.every(20).minutes.do(water)
schedule.every(30).minutes.do(eyes)
schedule.every(45).minutes.do(py)
while True:
     schedule.run_pending()
     time.sleep(1)




