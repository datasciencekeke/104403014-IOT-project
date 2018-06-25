import pyaudio
import speech_recognition as sr
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIOpinRed = 2
GPIOpinGreen = 3
GPIOpinYellow = 4
GPIO.setup(GPIOpinRed,GPIO.OUT)
GPIO.setup(GPIOpinGreen,GPIO.OUT)
GPIO.setup(GPIOpinYellow,GPIO.OUT)

camera = PiCamera()

#obtain audio from the microphone
r=sr.Recognizer()
r.energy_threshold=2000

GPIO.output(GPIOpinRed,False)
GPIO.output(GPIOpinGreen,False)
GPIO.output(GPIOpinYellow,False)

my_stt=""
while my_stt!="離開":
    try:
        with sr.Microphone() as source:
          print("Please wait. Calibrating microphone...") 
        #listen for 5 seconds and create the ambient noise energy level 
          r.adjust_for_ambient_noise(source, duration=3) 
          print("Say something!")
          audio = r.listen(source)

        # recognize speech using Google Speech Recognition 

        my_stt=r.recognize_google(audio, language="zh-TW")
        print(my_stt)
        
        if my_stt=="打開紅色的LED燈":
            GPIO.output(GPIOpinRed,True)
        elif my_stt=="打開黃色的LED燈":
            GPIO.output(GPIOpinYellow,True)
        elif my_stt=="打開綠色的LED燈":
            GPIO.output(GPIOpinGreen,True)
        elif my_stt=="關掉紅色的LED燈":
            GPIO.output(GPIOpinRed,False)
        elif my_stt=="關掉黃色的LED燈":
            GPIO.output(GPIOpinYellow,False)
        elif my_stt=="關掉綠色的LED燈":
            GPIO.output(GPIOpinGreen,False)
        elif my_stt=="拍照":
            camera.start_preview()
            sleep(5)
            camera.capture('/home/pi/Desktop/image.jpg')
            camera.stop_preview()
        elif my_stt=="離開":
            GPIO.output(GPIOpinRed,False)
            GPIO.output(GPIOpinYellow,False)
            GPIO.output(GPIOpinGreen,False)
            print("bye bye!")
            break
    except sr.UnknownValueError:
         print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
         print("No response from Google Speech Recognition service;{0}".format(e))
