#!/usr/bin/env python2.6

MAX_ALT = 9999

def elevationMatrix(lines):
	matrix = []
	for line in lines:
		row = [int(alt) for alt in line.split(" ")]
		matrix.append(row)
	return matrix

def calculateFlows(elevationMatrix, numRows, numCols):
	flowMatrix = []
	for r in range(numRows):
		flowRow = []
		for c in range(numCols):
			direction = getDirection(elevationMatrix, r, c, numRows, numCols)
			flowRow.append(direction)
		flowMatrix.append(flowRow)
	return flowMatrix

def getDirection(elevationMatrix, row, col, numRows, numCols):
	alt = elevationMatrix[row][col]
	north = elevationMatrix[row-1][col] if row-1 >= 0 else MAX_ALT + 1
	west = elevationMatrix[row][col-1] if col-1 >= 0 else MAX_ALT + 1
	east = elevationMatrix[row][col+1] if col+1 < numCols else MAX_ALT + 1
	south = elevationMatrix[row+1][col] if row+1 < numRows else MAX_ALT + 1
	low = min(alt, north, west, east, south)
	if low == alt: return "0"
	if low == north: return "^"
	if low == west: return "<"
	if low == east: return ">"
	if low == south: return "V"

def markFlows(flowMatrix, numRows, numCols):
	nextBasin = 'a'
	for r in range(numRows):
		for c in range(numCols):
			flowMatrix = markFlow(flowMatrix, r, c, nextBasin)
			if flowMatrix[r][c] == nextBasin:
				nextBasin = chr(ord(nextBasin)+1)
	return flowMatrix

def markFlow(flowMatrix, row, col, nextBasin):
	direction = flowMatrix[row][col]
	if direction == "0":
		flowMatrix[row][col] = nextBasin
	elif not direction.islower():
		nextCol = col + (direction == ">") - (direction == "<")
		nextRow = row + (direction == "V") - (direction == "^")
		flowMatrix = markFlow(flowMatrix, nextRow, nextCol, nextBasin)
		flowMatrix[row][col] = flowMatrix[nextRow][nextCol]
	return flowMatrix

def printBasins(basinMatrix):
	for basinRow in basinMatrix:
		print " ".join(basinRow)

import sys
lines = sys.stdin.read().split("\n")

numTestCases = int(lines[0])
lines = lines[1:]
linenr = 0

for testCase in range(numTestCases):
	size = lines[linenr].split(" ")
	numRows = int(size[0])
	numCols = int(size[1])
	caseRows = lines[linenr+1 : linenr+1+numRows]
	linenr += numRows + 1
	
	elevationMap = elevationMatrix(caseRows)
	flowMatrix = calculateFlows(elevationMap, numRows, numCols)
	basinMatrix = markFlows(flowMatrix, numRows, numCols)
	print "Case #" + str(testCase + 1) + ":"
	printBasins(basinMatrix)
