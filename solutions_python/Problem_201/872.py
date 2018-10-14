#!/usr/bin/python

import requests, logging, string, sys, heapq

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def processResults(stalls, user):
	heap = []
	countmap = {}
	heapq.heappush(heap, -stalls)
	countmap[-stalls] = 1
	first = 0
	second = 0
	count = 1
	while len(heap) > 0 and count <= user:
		element = heapq.heappop(heap)
		elementcount = countmap[element]
		#print "element", str(element), "elementcount", str(elementcount)
		count = count + elementcount
		countmap.pop(element, None)

		first = -element/2
		first = -first
		second = first
		if element % 2 == 0:
			second = first + 1

		if not first in countmap:
			countmap[first] = 0
			heapq.heappush(heap, first)

		if not second in countmap:
			countmap[second] = 0
			heapq.heappush(heap, second)

		countmap[first] = countmap[first] + elementcount
		countmap[second] = countmap[second] + elementcount
		#print "first", str(first), "second", str(second), "count", str(count)
			
	return str(abs(first)) + ' ' + str(abs(second))


def processInput(inputlines):
	results = []
	count = 0
	for datamap in inputlines:
		result = processResults(datamap['stalls'], datamap['user'])
		count = count + 1
		print "result", result, "test#", str(count)
		#print "***************************************************************************"
		results.append(result)
	return results

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		datamap = {}
		values = f.readline().split(' ')
		datamap['stalls'] = int(values[0].strip())
		datamap['user'] = int(values[1].strip())
		inputlines.append(datamap)
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	results = processInput(inputlines)
	createOutput(results)
	sys.exit()
