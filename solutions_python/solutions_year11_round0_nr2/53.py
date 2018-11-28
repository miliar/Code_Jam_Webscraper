#!/usr/bin/python
import sys


infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	line = infile.readline().split()
	
	combines = []
	numCombines = int(line.pop(0))
	for i in range(numCombines):
		combines.append(line.pop(0))
	
	opposes = []
	numOpposes = int(line.pop(0))
	for i in range(numOpposes):
		opposes.append(line.pop(0))
	
	numInvokes = int(line.pop(0))
	elements = list(line.pop(0))
	elementList = []
	
	for element in elements:
		elementList.append(element)
		processing = True
		while processing:
			processing = False
			if len(elementList) < 2:
				break
			for i in combines:
				if ((elementList[-2] == i[0] and elementList[-1] == i[1])
					or (elementList[-2] == i[1] and elementList[-1] == i[0])):
					elementList = elementList[:-2] + [i[2]]
					processing = True
					break
			if not processing:
				for i in opposes:
					if i[0] in elementList and i[1] in elementList:
						index = max(elementList.index(i[0]), elementList.index(i[1]))
						elementList = elementList[index+1:]
						processing = True
						break
	
	outStr = ""
	for i in range(len(elementList)):
		outStr += elementList[i]
		if i != len(elementList)-1:
			outStr += ", "
	print "Case #%s: [%s]" % (caseNum, outStr)
