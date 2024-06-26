from tkinter import *
from tkinter import filedialog

import PIL.Image
import google.generativeai as genai
from PIL import ImageTk


def startwork():

    filepath = filedialog.askopenfilename(
        initialdir="/home"
    )
    print(filepath)
    img = PIL.Image.open(filepath)
    resized = img.resize((300, 150))
    photo = ImageTk.PhotoImage(resized)
    display.config(image=photo)
    genai.configure(api_key="AIzaSyAnU_UhPcPT42NOArbr251CAiqCopPp3X8")
    model = genai.GenerativeModel("gemini-pro-vision")
    prompt = prompt_entry.get()
    response = model.generate_content((prompt, img))
    result.config(text=response.text)
    print(response.text)


window = Tk()

window.geometry("400x400")

prompting = Label(text="Enter your prompt")
prompting.pack()

prompt_entry = Entry(window)
prompt_entry.pack()

openButton = Button(text="Open", command=startwork)
openButton.pack()

display = Label(window)
display.pack()

result = Label(window, text="")
result.pack()

window.mainloop()