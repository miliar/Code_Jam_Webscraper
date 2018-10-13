#!/usr/bin/python

import requests, logging, string, sys

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + str(result[i]) + "\n")
	f.close();
	return

def processResults(statearray):
	additions = 0
	total = 0
	for i in range(0, len(statearray)):
		if total < i:
			additions = additions + (i - total)
			total = i
		total = total + statearray[i]
	return additions

def processInput(inputlines):
	result = []
	for line in inputlines:
		values = line.split(' ')
		Smax = int(values[0])
		state = values[1]
		statelist = list(state)
		statearray = []
		for item in statelist:
			statearray.append(int(item))
		additions = processResults(statearray)
		result.append(additions)
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
