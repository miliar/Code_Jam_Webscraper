#!/usr/bin/python

import requests, logging, string, sys

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def createHappyFacePackaces():
	return "+" * 1000

def processResults(pancakes, flipsize, happyFaces):
	if pancakes in happyFaces:
		return "0"

	totalCakes = len(pancakes)
	flips = 0
	pancakes = list(pancakes)
	#print totalCakes
	for i in range(0, totalCakes):
		#print pancakes, str(i + flipsize)
		if pancakes[i] == '-' and (i + flipsize) <= totalCakes:
			flips = flips + 1
			for j in range(i, i + flipsize):
				if pancakes[j] == '+':
					pancakes[j] = '-'
				else:
					pancakes[j] = '+'

	if ''.join(pancakes) in happyFaces:
		return str(flips)
	return "IMPOSSIBLE"


def processInput(inputlines):
	happyFaces = createHappyFacePackaces()
	results = []
	count = 0
	for datamap in inputlines:
		pancakes = datamap['pancakes']
		flipsize = datamap['flipsize']
		result = processResults(pancakes, flipsize, happyFaces)
		count = count + 1
		#print result, count
		results.append(result)
	return results

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		values = f.readline().strip().split(' ')
		datamap = {}
		datamap['pancakes'] = values[0]
		datamap['flipsize'] = int(values[1])
		inputlines.append(datamap)
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	results = processInput(inputlines)
	createOutput(results)
	sys.exit()
