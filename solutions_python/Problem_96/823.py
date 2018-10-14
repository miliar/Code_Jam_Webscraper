#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import ceil, floor
 
def line2intlist(line):
	list = line.split(' ')
	numbers = [ int(x) for x in list ]
	return numbers

def getDist(points, isSurp=False):
	p = floor(points / 3.0)
	trip = [p, p, p]
	if 3*p < points:
		trip[0] += 1
	if (3*p + 1) < points:
		trip[1] += 1

	trip.sort(reverse=True)

	if isSurp and (trip[1] == trip[0]) and trip[1] > 0:
		trip[1] -= 1
		trip[0] += 1
		trip.sort(reverse=True)

	return trip
 
def maxGooglers(nrOfGooglers, surprising, p, points):
	mg = 0
	surp = 0
	for pi in points:
		trip = getDist(pi, True)
		if ceil(pi/3.0) >= p:
			mg += 1
		elif trip[0] >= p:
			surp += 1
	
	mg += min(surp, surprising)

	return mg
 
if __name__ == "__main__":
	testcases = input()
 
	for caseNr in xrange(0, testcases):
		originalList = line2intlist(raw_input())
		nrOfGooglers = originalList[0]
		surprising = originalList[1]
		p = originalList[2]
		points = originalList[3:]
		print("Case #%i: %i" % (caseNr+1, maxGooglers(nrOfGooglers, surprising, p, points)))
