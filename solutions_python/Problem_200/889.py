#!/usr/bin/python

import requests, logging, string, sys

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def processResults(numStr):
	if len(numStr) == 1:
		return numStr

	numList = []
	for digit in numStr:
		numList.append(int(digit))
	#print numList

	isTidy = True
	for num in numList:
		if num != numList[0]:
			isTidy = False
			break

	if isTidy:
		return numStr

	numlen = len(numList)
	for i in range(1, numlen):
		if numList[i - 1] > numList[i]:
			for j in range(0, numlen):
				if numList[j] == numList[i - 1]:
					numList[j] = numList[j] - 1
					for k in range(j + 1, numlen):
						numList[k] = 9
					break
			break

	num = int(''.join(map(str,numList)))
	return str(num)


def processInput(inputlines):
	results = []
	count = 0
	for numStr in inputlines:
		result = processResults(numStr)
		count = count + 1
		#print result, count
		results.append(result)
	return results

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		inputlines.append(f.readline().strip())
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	results = processInput(inputlines)
	createOutput(results)
	sys.exit()
