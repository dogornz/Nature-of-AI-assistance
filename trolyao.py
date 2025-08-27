import pyttsx3
import speech_recognition
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer() #initial robot ear
robot_mouth = pyttsx3.init() #initial robot ear
robot_brain = "" #initial robot brain

you = ""

while True:
	###EAR
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	###BRAIN
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you == ""
	print("You:", you)

	if you == "":
		robot_brain = "I can't hear you, try again !"
	elif "hello" in you:
		robot_brain = "Hello Nguyen Dat !"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now();
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
        #RATE: speed of the volume
		robot_brain = "Bye Nguyen Dat"
		rate = robot_mouth.getProperty('rate')
		rate = robot_mouth.setProperty('rate', 150)

		#VOLUME: strength of voice
		volume = robot_mouth.getProperty('volume')
		volume = robot_mouth.setProperty('volume', 1.0) #between 0 and 1

		#VOICE: male or female
		voices = robot_mouth.getProperty('voices')
		#voices = robot_brain.setProperty('voice', voices[0].id)
		voices = robot_mouth.setProperty('voice', voices[1].id)

		#TEST
		print("Robot:", robot_brain)
		robot_mouth.say(robot_brain) # initial robot mouth
		robot_mouth.runAndWait() 
		break
	else:
		robot_brain = "I'm fine thank you and you ?"

	#RATE: speed of the volume
	rate = robot_mouth.getProperty('rate')
	rate = robot_mouth.setProperty('rate', 150)

	#VOLUME: strength of voice
	volume = robot_mouth.getProperty('volume')
	volume = robot_mouth.setProperty('volume', 1.0) #between 0 and 1

	#VOICE: male or female
	voices = robot_mouth.getProperty('voices')
	#voices = robot_brain.setProperty('voice', voices[0].id)
	voices = robot_mouth.setProperty('voice', voices[1].id)

	#TEST
	print("Robot:",robot_brain)
	robot_mouth.say(robot_brain) # initial robot mouth
	robot_mouth.runAndWait() 