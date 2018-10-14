#!/usr/bin/python

normal = "abcdefghijklmnopqrstuvwxyz"
trans = "ynficwlbkuomxsevzpdrjgthaq"

f = open("A-small-attempt0.in", "r")

numberOfTestCases = 0
caseNumber = 1;
myOutputString = ""

for line in f:
	if numberOfTestCases==0 : numberOfTestCases = line.rstrip()
	else :
		myOutputString = "Case #" + str(caseNumber) + ": "
		caseNumber = caseNumber + 1
		iS = line.rstrip()
		for c in iS:
			if normal.count(c):
				myOutputString = myOutputString + normal[trans.index(c)]
			else:
				myOutputString = myOutputString + c
		print myOutputString