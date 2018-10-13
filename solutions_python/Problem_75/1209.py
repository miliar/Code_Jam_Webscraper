#!/usr/bin/env python

# This code is not intended to be pretty or good,
# it just solves the problem. There are strings inside
# the code instead of using constants... That kind
# of things. Bare with it. 

import sys
from os.path import isfile

baseElements = ["Q", "W", "E", "R", "A", "S", "D", "F"]

def usage():
	print("CodeJam 2011 Magicka program. Usage: ")
	print("./Magicka.py <inputFile>")
	print("")
	sys.exit(1)

def malformed():
	print("Input file malformed")
        print("")
        sys.exit(2)	

def treatCase(caseNumber,caseString):	
	# variables
	matchedElements = dict()
	inverseElements = dict()
	for element in baseElements:
		matchedElements[element] = dict()
		inverseElements[element] = []
	elementList = []
	tokens = caseString.split()
	# read matchedElements
	numElems = int(tokens[0])
	elems = tokens[1:numElems+1]
	for elem in elems:
		matchedElements[elem[0]][elem[1]]=elem[2]
		matchedElements[elem[1]][elem[0]]=elem[2]

	tokens = tokens[numElems+1:]
	# read inverseElements
	numElems = int(tokens[0])
	elems = tokens[1:numElems+1]
	for elem in elems:
		inverseElements[elem[0]].append(elem[1])
		inverseElements[elem[1]].append(elem[0])
	
	tokens = tokens[numElems+1:]
	# read Elements
	elemString = tokens[1]
	for elem in elemString:
		inserted = False
		if (matchedElements[elem]):
			if elementList:
				elemc = elementList[-1]
				if elemc in matchedElements[elem]:
					elementList.pop()
					elementList.append(matchedElements[elem][elemc])
					inserted = True
				
		if(inverseElements[elem] and not inserted):
			for elemc in inverseElements[elem]:
				if elementList.count(elemc) > 0:
					del elementList[:]
					inserted = True
		
		if not inserted:
			elementList.append(elem)
	
	print ("Case #" +  str(caseNumber) + ": " + str.replace(str(elementList),'\'',''))	

if (len(sys.argv) < 2 ):
	usage()
	
if not isfile(sys.argv[1]):
	usage()

with open (sys.argv[1] , 'r') as f:
	lines = f.readlines()

testCases = int ( lines[0] )
if ( len(lines)-1 != testCases):
	malformed()
 
currentCase = 1
while ( currentCase <= testCases ):
	treatCase(currentCase,lines[currentCase])
	currentCase=currentCase+1


