#!/usr/bin/env python2.6

def minCoins(line1, line2):
	prisoners = line2.split(" ")
	for i in range(len(prisoners)):
		prisoners[i] = int(prisoners[i])
	(cells, release) = line1.split(" ")
	numCells = int(cells)
	cells = []
	for i in range(numCells):
		cells.append(1)
	return minRelease(prisoners, cells)

def minRelease(prisoners, cells):
	minCoins = 1e10
	bestPrisoner = -1
	for prisoner in prisoners:
		if len(prisoners) > 1:
			p = prisoners[:]
			p.remove(prisoner)
			c = cells[:]
			c[prisoner-1] = 0
			nextReleasesCost = minRelease(p, c)
		else:
			nextReleasesCost = 0
		thisReleaseCost = countCoins(prisoner, cells)
		coins = thisReleaseCost + nextReleasesCost
		if coins < minCoins:
			minCoins = coins
			bestPrisoner = prisoner
	return minCoins

def countCoins(prisoner, cells):
	rslt = 0
	r = range(prisoner-1)
	r.reverse()
	for i in r:
		if cells[i] == 0: break
		rslt += 1
	for i in range(prisoner, len(cells)):
		if cells[i] == 0: break
		rslt += 1
	return rslt

import sys
lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])
lines = lines[1:]
for testCase in range(numTestCases):
	(line1, line2) = lines[2*testCase:2*(testCase+1)]
	output = minCoins(line1, line2)
	print "Case #" + str(testCase + 1) + ": " + str(output)
