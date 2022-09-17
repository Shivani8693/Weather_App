from asyncore import read
from tkinter import *
import tkinter as tk
from turtle import color
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz
from PIL import ImageTk, Image

root=tk.Tk()
root.title('Weather App')
root.geometry("530x500")
root.resizable(False,False)

def getWeather():
    try:
        city=textField.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj =TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current time")

    #api
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a1e1232167941dd5ae32b168ef2b1d55"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]["main"]
        description=json_data['weather'][0]['main']
        temp=int(json_data['main']['temp']-279.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Input")

#background image
frame = Frame(root, width=900, height=600)
frame.pack()
frame.place(anchor=CENTER, relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open('background.png'))
label = Label(frame, image = img,bg='lightgreen',border=10)
label.pack()

#title
label1=Label(root,text="  mansum  ",font=("TimeNewRoman",45,"italic bold"),bg="#36b4eb",fg="#edf720")
label1.place(x=60,y=20,width=400,height=50)

#search box
search_image=PhotoImage(file='search bar.png')
myimage=Label(image=search_image,anchor=CENTER)
myimage.place(x=20,y=100,height=50)

textField=tk.Entry(root,justify="center",width=15,font=("poppins",16,"bold"),border=2,bg="lightblue",fg="darkblue")
textField.place(x=70,y=110)
textField.focus()

#search icon
search_icon=PhotoImage(file="search_icon.png")
myimage=Button(image=search_icon,cursor="hand2",border=1,bg="#e8e6d3",command=getWeather)
myimage.place(x=245,y=100,width=44,height=50)

#icon
weather_logo=PhotoImage(file="icon.png")
myimage=Label(image=weather_logo,cursor="hand2",border=3,borderwidth=3,justify=CENTER)
myimage.place(x=20,y=100,width=50,height=50)

#search box
box=PhotoImage(file='box.png')
myimage=Label(image=box,border=4)
myimage.place(y=392,width=550,height=100)

#time label
name=Label(root,font=("arial,",16,"bold"),fg="#820707",bg="#029ad1")
name.place(x=21,y=160)
clock=Label(root,font=("arial,",14,"bold"),fg="#80146f",bg="#029ad1")
clock.place(x=21,y=190)

# base label
label1=Label(root,text="WIND",font=("TimeNewRoman",15,"bold"),bg="#0ebbc4",fg="black")
label1.place(x=35,y=415)

label1=Label(root,text="HUMIDITY",font=("TimeNewRoman",15,"bold"),bg="#0ebbc4",fg="black")
label1.place(x=120,y=415)

label1=Label(root,text="DESCRIPTION",font=("TimeNewRoman",15,"bold"),bg="#0ebbc4",fg="black")
label1.place(x=245,y=415)

label1=Label(root,text="PRESSURE",font=("TimeNewRoman",15,"bold"),bg="#0ebbc4",fg="black")
label1.place(x=400,y=415)


t=Label(font=("arial",38,"bold"),fg="#b83116",bg="#c2e5f2")
t.place(x=350,y=250)
c=Label(font=("arial",16,"bold"),fg="#d1671b",bg="#afdced")
c.place(x=280,y=302)

w=Label(text=".....",font=("arial",17,"bold"),fg="#578191",bg="#0ebbc4")
w.place(x=40,y=445)
h=Label(text=".....",font=("arial",17,"bold"),fg="#4c6670",bg="#0ebbc4")
h.place(x=150,y=445)
d=Label(text=".....",font=("arial",17,"bold"),fg="#425359",bg="#0ebbc4")
d.place(x=300,y=445)
p=Label(text=".....",font=("arial",17,"bold"),fg="#32444a",bg="#0ebbc4")
p.place(x=450,y=445)

root.mainloop()

