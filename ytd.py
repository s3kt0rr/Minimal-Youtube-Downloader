import tkinter
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import urllib.request 
from pytube import YouTube
import wget

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry(f"{800}x{500}")
app.title("Minimal Youtube Downloader")
app.configure(background = 'white')
link_var = tk.StringVar()



# Create a photoimage object of the image in the path
image1 = Image.open("./img/ytd_logo.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
#Position image
label1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

#Download_FUNCTION
def button_function():
    print("button pressed")
    linko = link_var.get()
    yt = YouTube(linko)
    yd = yt.streams.get_highest_resolution()

    yd.download('C:/MYTD/Videos')


def browse_function():
    print("Button Pressed")
    filepath = filedialog.askopenfilename(initialdir="C:\MYTD/Videos",
                                          title="Here are your Downloads :")
                                    
    file = open(filepath,'r')
    print(file.read())
    file.close()


#Search_FUNCTION
def search_one():
    linko = link_var.get()
    yt = YouTube(linko)

    label = customtkinter.CTkLabel(master=app, text="Title : ")
    label.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

    text_var1 = tkinter.StringVar(value= yt.title)

    label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var1,
                               width=220,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




    text_var2 = tkinter.StringVar(value= yt.views)
    
    label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var2,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
    label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    label = customtkinter.CTkLabel(master=app, text="Views : ")
    label.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
  
    label = customtkinter.CTkLabel(master=app, text="Length : ")
    label.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

    text_var4 = tkinter.StringVar(value=yt.length)

    label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var4,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
    label.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

"""""
    imageUrl = text_var3
    u = urlopen(imageUrl)
    raw_data = u.read()         #DISPLAY_IMAGE_FROM_LINK
    u.close()

    photo = ImageTk.PhotoImage(data=raw_data)
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()
"""""

#Label_For_Pasting_YT_Links
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Paste The YouTube Video Link Here : ",
                               textvariable=link_var,
                               width=500,
                               height=35,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)


#ThumbNail_Downloader

def thumb_dow():
    linko = link_var.get()
    id = linko.split("=",1)[1]
    thumbnailurl= 'https://img.youtube.com/vi/'+id + '/maxresdefault.jpg'
    path = 'C:/MYTD/Thumbs'
    thumbnail = wget.download(thumbnailurl, path)


#Search_Button
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Search",
                                 command=search_one)
button.place(relx=0.9, rely=0.3, anchor=tkinter.CENTER)

#Thumb_Download_Button
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Thumb Download",
                                 command=thumb_dow)
button.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)


#Download_Button
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Download",
                                 command=button_function)
button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#Browse_Button
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Browse",
                                 command=browse_function)
button.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)

app.mainloop()