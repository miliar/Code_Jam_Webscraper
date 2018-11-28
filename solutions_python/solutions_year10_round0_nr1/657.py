#!/usr/bin/env python
import sys
import os
import string

def snapper(iNumSnappers, iSnaps):
	if ((2**iNumSnappers)-1 & iSnaps) == (2**iNumSnappers) - 1:
		return "ON"
	else:
		return "OFF"

def main():
	file = sys.argv[1]
	currentTestCase = 1
	with open(file) as f:
		testCaseCount = int(f.readline())
		for counter in range(testCaseCount):
			sTestLine = f.readline()
			iN = int(string.split(sTestLine,' ')[0])
			iK = int(string.split(sTestLine,' ')[1])
			print "Case #%(caseNumber)d: %(output)s" % {'caseNumber': counter + 1, 'output': snapper(iN, iK)}

if __name__ == "__main__":
	main()


