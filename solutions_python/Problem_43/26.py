#!/usr/bin/env python2.6

def getDict(line):
	rslt = {}
	rslt[line[0]] = 1
	nxtValue = 0
	for char in line:
		if not rslt.has_key(char):
			rslt[char] = nxtValue
			nxtValue += (2 if nxtValue == 0 else 1)
	return rslt

def minSeconds(line):
	dct = getDict(line)
	base = max(2, len(dct))
	rslt = 0
	length = len(line)
	for i in range(len(line)):
		rslt += dct[line[i]] * (base ** (length -1 - i))
	return rslt

import sys
lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])
lines = lines[1:]

for testCase in range(numTestCases):
	line = lines[testCase]
	output = minSeconds(line)
	print "Case #" + str(testCase + 1) + ": " + str(output)
