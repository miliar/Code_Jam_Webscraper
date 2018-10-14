#!/usr/bin/python

import sys

def processCase(iSize,motes):
	# *** BEGIN CODE PROCESSING CASE ***

	while len(motes)>0:
		if iSize>motes[0]:
			mote=motes.pop(0)
			iSize=iSize+mote
		else:
			mote=motes.pop(0)
			motes2=motes[:]
			resA=int(processCase(iSize,motes2))
			if iSize>1:
				motes2=motes[:]
				motes2.insert(0,mote)
				motes2.insert(0,iSize-1)
				resB=int(processCase(iSize,motes2))
			else:
				resB=resA
			if resA>resB:
				return str(1+resB)
			else:
				return str(1+resA)

	# *** END CODE PROCESSING CASE ***
	return "0"

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()

	initialSize=int(caseInput.split()[0])

	caseInput=sys.stdin.readline()
	motes=map(int,caseInput.split())
	motes.sort()
		
	# *** END CODE READING CASE ***

	solution=processCase(initialSize,motes)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

