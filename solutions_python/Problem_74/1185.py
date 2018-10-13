'''
Created on May 7, 2011

@author: Nathan V-C
'''

import Queue

def parseTestLine(testLine):
	orangeQ = Queue.Queue()
	blueQ = Queue.Queue()
	turnQ = Queue.Queue()
	
	test = testLine.split(" ")
	
	numButtons = int(test[0])
	
	i = 1
	while i < len(test) - 1:
		color = test[i]
		button = int(test[i + 1])
		
		if color == 'O':
			orangeQ.put(button)
			turnQ.put('O')
		else:
			blueQ.put(button)
			turnQ.put('B')
			
		i+=2
	
	return turnQ, orangeQ, blueQ

def getNumSteps(turnQ, orangeQ, blueQ):
	steps = 0
	
	posO = posB = 1
	
	turn = nextO = nextB = None
	
	while orangeQ.qsize() > 0 or nextO != None or blueQ.qsize() > 0 or nextB != None:
		if nextO == None and orangeQ.qsize() > 0:
			nextO = orangeQ.get()
			
		if nextB == None and blueQ.qsize() > 0:
			nextB = blueQ.get()
		
		if turn == None and turnQ.qsize() > 0:
			turn = turnQ.get() 
		
		if nextO != None:
			if posO == nextO:
				if turn == 'O':
					nextO = turn = None
			else:
				dist = nextO - posO
				posO += dist / abs(dist)
		
		if nextB != None:
			if posB == nextB:
				if turn == 'B':
					nextB = turn = None
			else:
				dist = nextB - posB 
				posB += dist / abs(dist)
				
		steps += 1
		
	return steps

def main(fileNameIn, fileNameOut):
	fIn = open(fileNameIn)
	fOut = open(fileNameOut, 'w')
	numTests = int(fIn.readline())
	
	for testNum in range(1, numTests + 1):
		turnQ, orangeQ, blueQ = parseTestLine(fIn.readline())
		numSteps = getNumSteps(turnQ, orangeQ, blueQ)
		
		outStr = "Case #%i: %i" % (testNum, numSteps)
		print outStr
		fOut.write(outStr + '\n')

main("A-large.in", "out")