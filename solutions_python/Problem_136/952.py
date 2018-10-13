#!/usr/bin/python

import sys



def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***
	C,F,X=map(float,case.split())

	myTime=0.0
	mySpeed=2.0

	while True:
		timetoX = X / mySpeed
		timetoFarm = C / mySpeed
		timetoXwithFarm = timetoFarm + (X / (mySpeed+F))

		if timetoX < timetoXwithFarm:
			return myTime+timetoX
		else:
			myTime = myTime + timetoFarm
			mySpeed = mySpeed + F

	# *** END CODE PROCESSING CASE ***
	return timetoX

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+str(solution)

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

