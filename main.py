from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("910x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    #weather
    api_url =f"https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=7ef40a42abf9ec92e4fcac424ff7b54f"
    
    #current 
    
    json_data = requests.get(api_url).json()

    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)
    
    #first cell
    
    firstdayimage = json_data['weather'][0]['icon']
    
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1
    
    Temp_Max1 = json_data['main']['temp_max']
    Temp_Min1 = json_data['main']['temp_min']
    
    day1temp.config(text=f"Temp:\nMax:{Temp_Max1}\nMin:{Temp_Min1}")
    
    #second cell
    
    seconddayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    
    Temp_Max2 = json_data['main']['temp_max']
    Temp_Min2 = json_data['main']['temp_min']
    
    day2temp.config(text=f"Temp:\nMax:{Temp_Max2}\nMin:{Temp_Min2}")
    
    #third cell
    
    thirddayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
    
    Temp_Max3 = json_data['main']['temp_max']
    Temp_Min3 = json_data['main']['temp_min']
    
    day3temp.config(text=f"Temp:\nMax:{Temp_Max3}\nMin:{Temp_Min3}")

    
    #fourth cell
    
    fourthdayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    
    Temp_Max4 = json_data['main']['temp_max']
    Temp_Min4 = json_data['main']['temp_min']
    
    day4temp.config(text=f"Temp:\nMax:{Temp_Max4}\nMin:{Temp_Min4}")
  
    
    #fifth cell
    
    fifthdayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    
    Temp_Max5 = json_data['main']['temp_max']
    Temp_Min5 = json_data['main']['temp_min']
    
    day5temp.config(text=f"Temp:\nMax:{Temp_Max5}\nMin:{Temp_Min5}")
    
    
   
    
    #sixth cell
    
    sixthdayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    
    Temp_Max6 = json_data['main']['temp_max']
    Temp_Min6 = json_data['main']['temp_min']
    
    day6temp.config(text=f"Temp:\nMax:{Temp_Max6}\nMin:{Temp_Min6}")

    
    #seventh cell
    
    seventhdayimage = json_data['weather'][0]['icon']
    
    img=(Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    
    Temp_Max7 = json_data['main']['temp_max']
    Temp_Min7 = json_data['main']['temp_min']
    
    day7temp.config(text=f"Temp:\nMax:{Temp_Max7}\nMin:{Temp_Min7}")
  
    
    #days
    
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    
    
    
    
    
    


# icon  Images\logo.png

image_icon = PhotoImage(file="Images\logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images\Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# label

label1 = Label(root, text="Temperature", font=("Helvetical", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetical", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=("Helvetical", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetical", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetical", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# search box

Search_image = PhotoImage(file="Images\Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="Images\Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root,justify="center",width=15, font=("poppins", 25, "bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="Images\Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243",command=getWeather)
myimage_icon.place(x=645, y=125)

# Bottom box

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)


# bottom boxes

firstbox = PhotoImage(file="Images\Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images\Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)

Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)

Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)

Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)

Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)

Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)

Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# clock (here we will place time)

clock = Label(root, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)


# timezone

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)



#temp, humi, pressure, wind, desc

t= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)

h= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)

p= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)

w= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)

d= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)


# First Place

firstframe = Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=38,y=315)

day1 = Label(firstframe,font="TimesNewRoman 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)

# Second Place

secondframe = Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=308,y=325)

day2 = Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2temp = Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=10,y=70)

# Third Place

thirdframe = Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=408,y=325)

day3 = Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp = Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=10,y=70)

# Fourth Place

fourthframe = Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=508,y=325)

day4 = Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp = Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=10,y=70)

# Fifth Place

fifthframe = Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=608,y=325)

day5 = Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp = Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=10,y=70)

# Sixth Place

sixthframe = Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=708,y=325)

day6 = Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp = Label(sixthframe,bg="#282829",fg="#fff")
day6temp.place(x=10,y=70)

#Seventh Place

seventhframe = Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=808,y=325)

day7 = Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage = Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp = Label(seventhframe,bg="#282829",fg="#fff")
day7temp.place(x=10,y=70)

root.mainloop()






