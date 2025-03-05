from gtts import gTTS
import os

import tkinter as tk
from tkinter import messagebox


class SpeechConverter:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Speech Converter")
        self.root.geometry("300x200")
        self.root.config(padx=10, pady=10)

        self.canvas = tk.Canvas(self.root, width=280, height=180)
        self.canvas.pack()

        self.entry = tk.Entry(self.root, width=35)
        self.canvas.create_window(133, 50, width=250, window=self.entry)

        # Create a Convert button and place it on the canvas
        self.convert_button = tk.Button(
            self.root, text="Convert to Speech", width=20,
            command=self.text_to_speech, highlightthickness=0
        )
        self.canvas.create_window(140, 80, window=self.convert_button)

        # Create an Exit button and place it on the canvas
        self.exit_button = tk.Button(
            self.root, text="Exit", width=20,
            command=self.root.quit, highlightthickness=0
        )
        self.canvas.create_window(140, 120, window=self.exit_button)

    def text_to_speech(self):
        text = self.entry.get()
        if not text:
            messagebox.showwarning("Warning", "No text provided for conversion.")
            return
        try:
            language = 'en'
            audio_output = gTTS(text=text, lang=language, slow=False)
            audio_output.save('audio_output.mp3')
            os.system('start audio_output.mp3')
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")


def main():
    root = tk.Tk()
    app = SpeechConverter(root)
    root.mainloop()


if __name__ == '__main__':
    main()
