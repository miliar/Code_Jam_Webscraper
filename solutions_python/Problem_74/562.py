#!/usr/bin/env python

from __future__ import print_function

import sys

def calcTime(moveList):

	totalTime = 0

	ORANGE = 1
	BLUE = 2

	bTime = 0
	oTime = 0

	bPos = 1
	oPos = 1

	inputRobot = -1

	for i in moveList:
		if (inputRobot == -1):
			if (i == "B"):
				inputRobot = BLUE
			elif (i == "O"):
				inputRobot = ORANGE
		else:
			newPos = int(i)
			
			if(inputRobot == BLUE):
				timeRequiredToMove = abs(newPos - bPos)
				bPos = newPos
				if (timeRequiredToMove + bTime >= totalTime):
					totalTime = timeRequiredToMove + bTime
				
				totalTime = totalTime + 1
				
				bTime = totalTime
				
			elif(inputRobot == ORANGE):
				timeRequiredToMove = abs(newPos - oPos)
				oPos = newPos
				
				if (timeRequiredToMove + oTime >= totalTime):
					totalTime = timeRequiredToMove + oTime
					
				totalTime = totalTime + 1
				
				oTime = totalTime
			inputRobot = -1
	
	return totalTime

if __name__ == "__main__":

	#print calcTime("O 2 B 1 B 2 O 4".split())
	#print calcTime("O 5 O 8 B 100".split())
	#print calcTime("B 2 B 1".split())
	if(len(sys.argv) != 3):
		print("Usage: %s inputfile outputfile" % sys.argv[0], file=sys.stderr)
		sys.exit(1)
		
	inputFile = open(sys.argv[1])
	outputFile = open(sys.argv[2], "w")
	
	numTestCases = int(inputFile.readline())
	
	for i in range(1, numTestCases+1):
		testCaseString = inputFile.readline()
		timeReqd = calcTime(testCaseString.split()[1:])
		outputFile.write("Case #%d: %d\n" % (i, timeReqd))
		
	inputFile.close();
	outputFile.close();
		