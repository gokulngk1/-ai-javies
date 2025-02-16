# import speech_recognition as aa 
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia

# listener = aa.Recognizer()

# machine = pyttsx3.init()


# def talk(text):
#     machine.say(text)
#     machine.runAndWait()

# def input_instruction():
#     global instruction
#     try:
#         with aa.Microphone() as origin:
#             print("listening...")
#             speech = listener.listen(origin)
#             instruction = listener.recognize_goggle(speech)     
#             instruction = instruction.lower()
#             if "Javies" in instruction:
#                 instruction = instruction.replace("Javies" ,"")
#                 print(instruction)
#     except Exception as e:
#         print(e)
#         pass
#     return instruction


# def play_Jarvis():
#     instruction = input_instruction()
#     print(instruction)
#     if "play" in instruction:
#         song = instruction.replace("play","")
#         talk("playing" + song)
#         pywhatkit.playsonyt(song)
#     elif 'time' in instruction:
#         time = datetime.datetime.now().strftime('%I:%M%p')
#         talk("current time" + time)
#     elif 'date' in instruction:
#         date = datetime.datetime.now().strftime('%d /%m /%Y')
#         talk("Today's date" + date)
#     elif 'how are you ' in instruction:
#         talk("I am fine how are you ")
#     elif 'What is your name ' in instruction:
#         talk("I am javies, what can i do for you")
#     elif 'Who is ' in instruction:
#         human = instruction.replace('Who is', "")
#         info = wikipedia.summary(human, 1)
#         print(info)
#         talk(info)
#     else:
#         talk("Please  repeat")
# play_Jarvis()


# import speech_recognition as aa
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia

# listener = aa.Recognizer()
# machine = pyttsx3.init()

# def talk(text):
#     machine.say(text)
#     machine.runAndWait()

# def input_instruction():
#     global instruction
#     try:
#         with aa.Microphone() as origin:
#             print("listening...")
#             speech = listener.listen(origin)
#             instruction = listener.recognize_google(speech)
#             instruction = instruction.lower()
#             if "Javies" in instruction:
#                 instruction = instruction.replace("Javies", "")
#                 print(instruction)
#     except Exception as e:
#         print(e)
#         pass
#     return instruction

# def play_Jarvis():
#     instruction = input_instruction()
#     print(instruction)
#     if "play" in instruction:
#         song = instruction.replace("play", "")
#         talk("playing " + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in instruction:
#         time = datetime.datetime.now().strftime('%I:%M%p')
#         talk("current time " + time)
#     elif 'date' in instruction:
#         date = datetime.datetime.now().strftime('%d /%m /%Y')
#         talk("Today's date " + date)
#     elif 'how are you' in instruction:
#         talk("I am fine, how are you?")
#     elif 'What is your name' in instruction:
#         talk("I am Javies, what can I do for you?")
#     elif 'Who is' in instruction:
#         human = instruction.replace('Who is', "")
#         info = wikipedia.summary(human, 1)
#         print(info)
#         talk(info)
#     else:
#         talk("Please repeat")

# play_Jarvis()

import speech_recognition as sr
import pyttsx3
import pywhatkit
# import pip install --no-cache-dir pyaudio

import datetime
import wikipedia

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    """Speaks the given text aloud."""
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Listens to user input via microphone and converts speech to text."""
    instruction = ""  # Initialize instruction to avoid reference issues
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            listener.adjust_for_ambient_noise(origin)  # Adjusts for background noise
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech).lower()  # Convert to lowercase
            
            if "javies" in instruction:  # Ensure "Javies" is recognized correctly
                instruction = instruction.replace("javies", "").strip()
                print(f"User said: {instruction}")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Could not connect to Google Speech Recognition.")
    except Exception as e:
        print(f"Error: {e}")
    
    return instruction

def play_jarvis():
    """Processes user commands and responds accordingly."""
    instruction = input_instruction()
    
    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    
    elif "time" in instruction:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {current_time}")
    
    elif "date" in instruction:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk(f"Today's date is {current_date}")
    
    elif "how are you" in instruction:
        talk("I am fine, how are you?")
    
    elif "what is your name" in instruction:
        talk("I am Javies, what can I do for you?")
    
    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        try:
            info = wikipedia.summary(human, sentences=1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results, please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information.")
    
    else:
        talk("I didn't understand, please repeat.")

# Run the assistant
play_jarvis()

