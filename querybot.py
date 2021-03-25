# QUERY CHATBOT FOR SCHOOLS MADE BY AYUSH BHUSHAN #
# NO EXTERNAL TOOLS ARE USED #
# FULL CODE #
import pyttsx3 # SPEAKING #
import speech_recognition as speech # LISTENING #
from time import sleep # STOP OR SLEEP #
s = speech.Recognizer()
engine=pyttsx3.init()
def say(words):
    engine.say(words)
    engine.runAndWait()
    print(words)
def listen():
    with speech.Microphone() as mi:
        print( "Listening......." )
        s.pause_threshold = 1
        audios = s.listen(mi)
    try:
        print( "Recognizing.......\n" )
        commands = s.recognize_google(audios, language='en-in')
        print(f"You said: {commands}\n")
    except Exception:
        return "None"
    return commands
say('Hello Everyone, I am a Question Bot and I am here to clear all your doubts related to the session 2021-2022')
say('But Remember, Everyting I say is only valid for the session 2021-2022 and may be changed anytime by the School.')
say("Let's Start, I am Listening.......")
while True:
    qns=listen().lower()
    if 'timings' in qns:
        say('The School Timings are as follows ------>\nNur to 5 :- 9 AM to 1 PM\n6 to 12 :- 8 AM to 2 PM')
        sleep(0.2)
    elif 'examination dates' in qns or 'exam dates' in qns or 'test dates' in qns:
        say('For All the Classes, Periodic Tests will be taken every Monday')
        sleep(0.2)
        say('The half-Yearly Exams will be conducted in the 2nd week of September')
        sleep(0.2)
        say('And the Annual Exams would be conducted in the last week of February')
        sleep(0.2)
    elif 'syllabus' in qns:
        say("The Detailed Syllabus is Already uploaded on the School's website")
        say('Here is the link :-')
        print("\n https://schoolwebste/syllabus/")
        sleep(0.2)
    elif 'offline' in qns or 'online' in qns or 'mode' in qns:
        say('As per the Guidelines Issued by the School, there will be OFFLINE Classes for Classes 8, 9, 10, 11 and 12')
        sleep(0.2)
        say('But for the Rest, the classes will continue in ONLINE MODE itself')
        sleep(0.2)
    elif 'classes schedule' in qns:
        say('There will be ONLINE classes for only 8 onwards, others WONT HAVE ONLINE classes')
        sleep(0.2)
        say('As per the Govt guidelines, the children would not be called on a regular basis but'
            ' alternatively and on the basis of ODD-EVEN formula')
        sleep(0.2)
        say('For example :- All the Odd roll numbers like- 1, 3, 5, etc.. would be called on the First day ')
        sleep(0.2)
        say('Rest Students would be called the next day and this process will Continue')
        sleep(0.2)
        say('The students are strictly to follow the Corona Guidelines issued by the Government')
        sleep(0.2)
        say( "Here's the link :-" )
        print('\n https://www.mohfw.gov.in/')
        sleep(0.2)
    elif 'guidelines' in qns:
        say("The detailed guidelines are mentioned the the government's website")
        sleep(0.2)
        say("Here's the link :-")
        print('\n https://www.mohfw.gov.in/')
        sleep(0.2)
    elif 'thank you' in qns or 'good' in qns or 'nice' in qns or 'keep it up' in qns:
        say("It's my pleasure to help you !!!")
        sleep(0.2)
    else:
        say('For further and detailed information, please contact the School')
        sleep(0.2)

# -----------------------------------------------END OF THE CODE-------------------------------------------------------#
