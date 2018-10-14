#!/usr/bin/python

import requests, logging, string, sys

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def processResults(X, R, C):
	volume = R * C
	if volume % X != 0:
		return "RICHARD"
	if X == 1 or X == 2:
		return "GABRIEL"
	if X == 3:
		if R == 1 or C == 1:
			return "RICHARD"
		else:
			return "GABRIEL"
	if X == 4:
		if (R == 4 and C == 4) or (R == 4 and C == 3) or (R == 3 and C == 4):
			return "GABRIEL"
		else:
			return "RICHARD"

def processInput(inputlines):
	result = []
	for line in inputlines:
		values = line.split(' ')
		X = int(values[0])
		R = int(values[1])
		C = int(values[2])
		result.append(processResults(X, R, C))
	return result

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		line = f.readline().strip()
		inputlines.append(line)
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	result = processInput(inputlines)
	createOutput(result)
	sys.exit()
