from gtts import gTTS
import os

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Speech Converter")
canvas = tk.Canvas(root, width=270, height=200)

canvas.pack()


def textToSpeech():
    text = entry.get()
    if not text:
        messagebox.showwarning("Warning", "No text selected for converting.")
        return

    language = 'en'
    audio_output = gTTS(text=text, lang=language, slow=False)
    audio_output.save('audio_output.mp3')
    os.system('start audio_output.mp3')


entry = tk.Entry(root)
canvas.create_window(133, 80, width=250, window=entry)
button = tk.Button(text="Start", width=15, command=textToSpeech)
canvas.create_window(135, 110, window=button)

exit_button = tk.Button(text="Exit", width=15, command=root.quit, highlightthickness=0)
canvas.create_window(135, 140, window=exit_button)

root.mainloop()
