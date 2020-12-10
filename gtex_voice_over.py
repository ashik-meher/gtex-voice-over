from gtts import gTTS
import os

gtex = "G Tex E R P.  The complete garments and textile E R P specially designed for RMG Industries. Request a demo today"

language = 'en'

output = gTTS(text=gtex, lang=language, slow=False)

output.save('output_gtex.mp3')

os.system('start output_gtex.mp3')
