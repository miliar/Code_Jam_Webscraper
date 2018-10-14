#! /usr/bin/python 

from gcj_io import *


def calcMaxSteps(steps):
	res=0
	Opos=1
	deltaO=0
	Bpos=1
	deltaB=0
	for i in range(len(steps)):
		step=steps[i]
		button=int(step[1])
		if step[0]=='O':
			#if abs(button-Opos)<(abs(button-Opos)+deltaO):
			if abs(button-Opos)< deltaO:
				res += 1
				deltaO = 0
				deltaB += 1
				Opos=button
			else:
				res += abs(button-Opos)- deltaO +1
				deltaB += abs(button-Opos)-deltaO +1
				deltaO = 0
				Opos = button
				
		else:
			#if abs(button-Bpos)<(abs(button-Bpos)+deltaB):
			if abs(button-Bpos)< deltaB:
				res += 1
				deltaB = 0
				deltaO += 1
				Bpos=button
			else:
				res += abs(button-Bpos)- deltaB +1
				deltaO += abs(button-Bpos)-deltaB +1
				deltaB = 0
				Bpos = button
					
			#~ if button==OPos:
				#~ res +=1
			#~ elif (button>OPos):
				#~ OPos+=button-OPos
				#~ res +=(button-OPos)+1
			#~ else:
				#~ OPos+=OPos-button
				#~ res +=(OPos-button)+1
		#~ else:
			#~ if button==BPos:
				#~ res +=1
			#~ elif (button>BPos):
				#~ BPos+=button-BPos
				#~ res +=(button-BPos)+1
			#~ else:
				#~ BPos+=BPos-button
				#~ res +=(BPos-button)+1
	return res
		
				
input=startExercise()
case = int(input[1])
file = input[0]
output = openOutput()
for i in range(case):
	command=getCase(file)
	nSteps=int(command[0])*2
	steps=[]
	for j in range(1,nSteps,2):
		step=[]
		step.append(command[j])
		j +=1
		step.append(command[j])
		steps.append(step)
	#print steps
	res=calcMaxSteps(steps)
	writeCase(i,output,res)
    
finishExercise(file,output)
print "Problem resolved!"
