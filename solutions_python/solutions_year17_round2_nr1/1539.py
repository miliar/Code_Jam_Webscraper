#!/usr/bin/python

import requests, logging, string, sys

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def calIntersection(distM, distY, speedM, speedY):
	return ((speedM * distY) - (speedY * distM))/(speedM - speedY)

def processResults(D, N, dmap):
	print D, N, dmap
	distances = list(dmap.keys())
	distances.sort()
	distM = distances[0]
	for i in range(1, N):
		speedM = dmap[distM]
		speedY = dmap[distances[i]]
		if speedM > speedY:
			distX = calIntersection(distM, distances[i], speedM, speedY)
			if distX < D:
				distM = distances[i]
				
	speed = float(D * dmap[distM])/float(D - distM)
	return "{:.6f}".format(speed)

def processInput(inputlines):
	results = []
	count = 0
	for datamap in inputlines:
		D = datamap['D']
		N = datamap['N']
		dmap = datamap['Dmap']
		result = processResults(D, N, dmap)
		count = count + 1
		print "Case ", count, ": ", result
		results.append(result)
	return results

def readinp(N, f):
	dmap = {}
	for j in range(0, N):
		ivalues = f.readline().strip().split(' ')
		distI = int(ivalues[0])
		dmap[distI] = int(ivalues[1])
	return dmap

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		values = f.readline().strip().split(' ')
		datamap = {}
		datamap['D'] = int(values[0])
		datamap['N'] = int(values[1])
		datamap['Dmap'] = readinp(datamap['N'], f)
		inputlines.append(datamap)
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	results = processInput(inputlines)
	createOutput(results)
	sys.exit()
