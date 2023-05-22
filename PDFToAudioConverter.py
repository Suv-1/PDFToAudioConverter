import pyttsx3 as py
import PyPDF2 as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


engine = py.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def open_file():
    file = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file)


def pdf_to_audio():
    pdfobj = file_entry.get()
    pdreader = pd.PdfReader(pdfobj)
    page = (len(pdreader.pages))

    for i in range(page):
        pageObj = pdreader.pages[i]
        extract_page = pageObj.extract_text()
        messagebox.showinfo("showinfo", extract_page)
        print(extract_page)
        speak(extract_page)


root = tk.Tk()
root.geometry("1000x800")
root.title("PDF to Audio Converter")
head = tk.Label(root, text="PDF to Audio Converter", padx=50, pady=50, font='Calibri 15')
head.pack()
file_label = tk.Label(root, text="PDF file: ", padx=20, pady=20, font='Calibri 10')
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()
file_button = tk.Button(root, text="Open the PDF File", font='Calibri 10', command=open_file)
file_button.pack()
convert_button = tk.Button(root, text="Convert to Audio", font='Calibri 10', command=pdf_to_audio)
convert_button.pack()

root.mainloop()
