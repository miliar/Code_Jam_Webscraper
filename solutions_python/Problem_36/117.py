#!/usr/bin/env python2.6

def readCase(case):
	rslt = {}
	for i in range(len(case)):
		char = case[i]
		if rslt.has_key(char):
			rslt[char].append(i)
		else:
			rslt[char] = [i]
	return rslt

def countPossibilities(charDict,  searchString,  case):
	rslt = []
	for char in searchString:
		if not charDict.has_key(char):
			return 0
		indices = charDict[char]
		if len(rslt) == 0:
			for i in range(len(case)):
				rslt.append(indices.count(i))
		else:
			n = range(len(rslt))
			n.reverse()
			for i in n:
				rslt[i] = indices.count(i) * sum(rslt[0:i])
	return sum(rslt)


import sys
lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])

testCases = lines[1:numTestCases+1]
casenr = 1
searchString = "welcome to code jam"

for case in testCases:
	charDict = readCase(case)
	numPossibilities = countPossibilities(charDict, searchString,  case)
	print "Case #" + str(casenr) + ": " + str(10000+numPossibilities)[-4:]
	casenr += 1
