from time import sleep #importing libraies needed for program
import guizero
import serial
from guizero import TextBox, App, PushButton, Slider

montr= serial.Serial("/dev/ttyACM0", 9600) #setup serialmonitor
montr.flush()
sleep(3)

Serv1pos=[]
Serv2pos=[]

def savepos(): #function for storing slidervals
    Serv1pos.append(servsetting1.value)
    Serv2pos.append(servsetting2.value)
    textbox1.value = servsetting1.value
    textbox2.value = servsetting2.value
    
    
def sliderread(sliderval1): #logic for moving servo1
    print(sliderval1)
    montr.flush()
    montr.write(str('M1').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    montr.write(str(sliderval1).encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    sleep(.2)
    

def sliderread2(sliderval2): #logic for moving servo2
    print(sliderval2)
    montr.flush()
    montr.write(str('M2').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    montr.write(str(sliderval2).encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    sleep(.2)


def repeatpos(): #function for returning servos to stored val
    for i in range(0,len(Serv1pos)):
        montr.write(str('M1').encode('utf-8'))
        montr.write(str("\n").encode('utf-8'))
        montr.flush()
        montr.write(str(Serv1pos[i]).encode('utf-8'))
        montr.write(str("\n").encode('utf-8'))
        montr.flush()

        montr.write(str('M2').encode('utf-8'))
        montr.write(str("\n").encode('utf-8'))
        montr.flush()
        montr.write(str(Serv2pos[i]).encode('utf-8'))
        montr.write(str("\n").encode('utf-8'))
        montr.flush()


app = App("Lab9") #starting and settingup app 

storebutton = PushButton(app, text="Store", command=savepos)
repeatbutton = PushButton(app, text="Repeat", command=repeatpos)
servsetting1 = Slider(app, start=0, end=180, width=300, command=sliderread)
servsetting2 = Slider(app, start=0, end=180, width=300, command=sliderread2)
textbox1=TextBox(app)
textbox2=TextBox(app)

app.display()
