#!/usr/bin/env python2.6

def readCase(line):
	rslt = []
	chrlist = list(line)
	while len(chrlist) > 0:
		chr = chrlist.pop(0)
		if chr != "(":
			rslt.append([chr])
		else:
			inBrackets = []
			chr = chrlist.pop(0)
			while chr != ")":
				inBrackets.append(chr)
				chr = chrlist.pop(0)
			rslt.append(inBrackets)
	return rslt

def countPossibilities(alienWords, charList):
	rslt = 0
	for alienWord in alienWords:
		if compare(alienWord, charList):
			rslt += 1
	return rslt

def compare(alienWord, charList):
	for i in range(len(alienWord)):
		alienChar = alienWord[i]
		possibleChars = charList[i]
		if not possibleChars.count(alienChar):
			return False
	return True


import sys
lines = sys.stdin.read().split("\n")
(wordLength,  numWords, numTestCases) = lines[0].split(" ")

wordLength = int(wordLength)
numWords = int(numWords)
numTestCases = int(numTestCases)

alienWords = lines[1:numWords+1]
casenr = 1
for case in lines[numWords+1:numWords+1+numTestCases]:
	charList = readCase(case)
	numPossibilities = countPossibilities(alienWords, charList)
	print "Case #" + str(casenr) + ": " + str(numPossibilities)
	casenr += 1
