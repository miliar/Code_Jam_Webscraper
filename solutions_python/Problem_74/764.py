import math
from math import *

file = open("input.txt")
i = int(file.readline())

string = ""
for case in range(i):
	array = file.readline().split()
	buttons = array[0]
	orangePos = 1
	bluePos = 1
	
	presses = array[1:]
	time = 0
	going = True
	
	nextPos = [-1,-1]
	currentPos = [1,1]

	test= len(presses)/2
	
	#find next poss
	for i in range(test):
		presses[i*2+1] = int(presses[i*2+1])
		
		if nextPos[0] == -1 and presses[i*2] == "O":
			nextPos[0] = presses[i*2+1]
			
		if nextPos[1] == -1 and presses[i*2] == "B":
			nextPos[1] = presses[i*2+1] 
	
	i = 0
	#print nextPos
	#print currentPos,nextPos
	
	noPress = False
	while test > i:
		noPress = False
		time += 1
		#move them too position
		for v in range(2):
			if nextPos[v] - currentPos[v] == 0 and noPress == False:
				if(currentPos[v] == int(presses[i*2+1])):
					letter = 'O'
					if v == 1:
						letter = "B"
					
					if(presses[i*2] == letter):
						i+=1
						noPress = True
						if(test > i):
							testI = i
							no = True
							while no == True and test > testI:
								if(presses[testI*2] == letter):
									nextPos[v] = presses[testI*2+1]
									no = False
								
								testI +=1
								
						
			else:
				if nextPos[v] - currentPos[v] > 0:
					currentPos[v] += 1
				elif nextPos[v] - currentPos[v] < 0:
					currentPos[v] -= 1
		#print currentPos,nextPos
 	print case
 	string += "Case #"+str(case+1)+": "+str(time)+"\n"
 
fileO = open("out.txt",'w')
fileO.write(string)
 

 
