# import of the required libraries
import os
from tkinter import *
from tkinter import filedialog  # to save the files
from tkinter.ttk import Combobox  # to create combobox/ dropdown

import pyttsx3  # the library that converts the text to speech

root = Tk()  # creation of the box
root.title("Text to Speech")  # title on the header
root.geometry("900x450+200+200")  # the size of the tab
root.resizable(False, False)  # the tab is not resizeable
root.configure(bg="#89a0d9")  # the background color

engine = pyttsx3.init()  # we use the pyttsx3 library for text to speech conversation


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    # the function speak now  make possible to convert the text to speech

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


image_icon = PhotoImage(file="speak.png")  # the icon in the header
root.iconphoto(False, image_icon)  # the line that shows the icon

Top_frame = Frame(root, bg="#d1dcf7", width=900, height=100)  # frame background and size
Top_frame.place(x=0, y=0)  # frame place

Logo = PhotoImage(file="speaker.png")  # logo in the frame
Label(Top_frame, image=Logo, bg="#d1dcf7").place(x=10, y=10)  # background color and place

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="#d1dcf7", fg="black").place(x=100, y=25)
# text that displays at the frame, font, background color, and text color

text_area = Text(root, font="arial 20", bg="#d1dcf7", relief=GROOVE, wrap=WORD)
# creating the text area, font of the text, background color, groove it gives a 3d visualization,
# the word = wrap it sends the word in another line when it does not fit
text_area.place(x=15, y=125, width=500, height=250)  # it shows the place and size of the text area

Label(root, text="VOICE", font="arial 15 bold", bg="#89a0d9", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#89a0d9", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')
#  it creates a dropbox with the male or female options,

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')
#  it creates a dropbox with the fast, normal, or slow options,

imageIcon = PhotoImage(file="speak.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageIcon, width=140, bg="#c8d9ff", font="arial 12 bold",
             command=speaknow)
btn.place(x=550, y=280)
# creating a button the text that contains the image width font and place
# also the command "speak now" we use for the function so the program functions

imageIcon2 = PhotoImage(file="download.png")
save = Button(root, text="Save", compound=LEFT, image=imageIcon2, width=140, bg="#c8d9ff", font="arial 12 bold",
              command=download)
save.place(x=730, y=280)

root.mainloop()  # lets the tkinter to show the application
