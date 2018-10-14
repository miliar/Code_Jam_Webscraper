#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case,start,end):
	sum = 0
	for val in range(start, end+1):
		# fair ?
		if checkPalindromes(val) == False:
			continue
		# squar ?
		sq = checkSquare(val)
		if sq == None:
			continue
		else:
			if checkPalindromes(sq) == False:
				continue
		sum = sum + 1
	return "Case #%d: %d\n" % (case,sum) 

def checkSquare(val):
	for i in range(1,val+1):
		sq = i * i
		if sq == val:
			return i
		elif sq > val:
			return None

def checkPalindromes(val):
	valStr = str(val)
	valStrList = list(valStr)
	right = deepcopy(valStrList)
	valStrList.reverse()
	left = deepcopy(valStrList)
	if right == left:
		return True
	else:
		return False

if __name__ == "__main__":
	isFirst = True
	inData = False

	totalCase = 0
	currentCase = 1 

	for line in inFile.readlines():
		items = line.split()

		# first Line
		if isFirst == True:
			isFirst = False
			totalCase = int(items[0])
			continue
		
		start = int(items[0])
		end = int(items[1])

		#print solve(currentCase, start, end)
		outFile.write(solve(currentCase, start, end))
		currentCase = currentCase + 1
		if currentCase > totalCase:
			break

		
