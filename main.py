from gtts import gTTS
import os

with open('demo.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()

language = 'en'

audio_output = gTTS(text=file_content, lang=language, slow=False)
audio_output.save('audio_output.mp3')

os.system('start audio_output.mp3')
