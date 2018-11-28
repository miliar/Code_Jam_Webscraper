#!/bin/python
import sys

fileName = sys.argv[1]

inputFile = open(fileName, 'r')
outputFile = open(fileName.strip('.in')+'.out', 'w')

numOfTestCases = int(inputFile.readline().strip())
print numOfTestCases
for i in xrange(numOfTestCases):
	line = inputFile.readline().strip()
	arr = line.split()
	n = int(arr[0])
	k = int(arr[1])
	value = 2**n
	result = (k - (value-1))% value
	if (result == 0):
		resultStr = "ON"
	else:
		resultStr = "OFF"
	outputFile.write('Case #'+str(i+1)+': '+resultStr+'\n')
inputFile.close()
outputFile.close()