import os
from gtts import gTTS


def text_to_speech(message, message_type):
    try:
        myText = message
        language = "en"
        obj = gTTS(text=myText, lang=language, tld="com.au", slow=False)
        obj.save(f"{message_type}.mp3")
        os.system(f"mpg321 {message_type}.mp3")
        os.remove(f"{message_type}.mp3")
    except Exception as e:
        print(f"EXCEPTION: {str(e)}")
