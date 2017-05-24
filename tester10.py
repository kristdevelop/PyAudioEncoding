# Base source of Python application ordered and supervised by Kylli Rist, developed by Arinde in 2012
# Kylli Rist, renewed this code for IT College Python Class in 2017 

import shlex, subprocess
import audioread			# from https://pypi.python.org/pypi/audioread/2.1.4

title = ""
i=0
f=open('mix_tofix.txt','r')
for line in f.readlines():
 i+=1
 line = line.replace('\n', '') # line replacement
 line = line.replace('\r', '') # line replacement
 command = "ffmpeg -y -i '" + line + "' test.mp3" # this is audio encoding
 args = shlex.split(command)
 p = subprocess.Popen(args) # success, jee
 p.wait()
 command = 'sox test.mp3 test.wav reverse silence 2 0.3 5% reverse'
 args = shlex.split(command)
 p = subprocess.Popen(args) # väga hea!
 p.wait()
 if p.returncode == 0:
     audio = audioread.audio_open('test.wav')
     with open("library.txt", "a") as myfile1:    # This is INPUT FILE for audio paths
       mytext1 = "%.2f" % (audio.duration) + '|'+line+'\n'
       myfile1.write(mytext1)
 if p.returncode != 0:
     with open("library.txt", "a") as myfile1:   # This is OUTPUT FILE
       mytext1 = str(p.returncode) + '|'+line+'\n'
       myfile1.write(mytext1)
 print mytext1
print "Good bye, done. It is March 24 already"
