#! /usr/bin/env python
import sys
import re

inputFile = sys.argv[1]


f = open(inputFile, 'r');

firstline = f.readline().strip()

#first line is meta data
[L,D,N] = firstline.split(" ");

#one word of length L
#D words
#N test cases

alienDict = []

for i in range(int(D)):
	alienDict.append(f.readline().strip())

testCases = []

for i in range(int(N)):
	testCase = f.readline().strip()
	#testCases.append(testCase)
	testCase = testCase.replace("(", "[")
	testCase = testCase.replace(")", "]")

	matchCount = 0
	for word in alienDict:
		if re.match(testCase, word):
			matchCount = matchCount + 1

	print "Case #"+str(i)+": "+str(matchCount)

#print testCases

