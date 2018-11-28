#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case,values):
	copyValues = deepcopy(values)

	# ‰¡
	for i in range(len(values)):
		height = max(values[i])
		for j in range(len(values[0])):
			if values[i][j] >= height:
				copyValues[i][j] = 0
	
	# c
	for j in range(len(values[0])):
		tempList = []
		for i in range(len(values)):
			tempList.append(values[i][j])
		height = max(tempList)
		for i in range(len(values)):
			if values[i][j] >= height:
				copyValues[i][j] = 0
	
	bImpossible = False
	for i in range(len(values)):
		for j in range(len(values[0])):
			if copyValues[i][j] > 0:
				bImpossible = True
				break
	
	if bImpossible == True:
		return "Case #%d: NO\n" % (case) 
	else:
		return "Case #%d: YES\n" % (case) 
	

if __name__ == "__main__":
	values = []		 
	
	isFirst = True
	inData = False

	totalCase = 0
	currentCase = 1 
	rowIndex = 0

	n = 0
	m = 0

	for line in inFile.readlines():
		items = line.split()

		# first Line
		if isFirst == True:
			isFirst = False
			totalCase = int(items[0])
			continue
		
		if inData == False:
			n = int(items[0])
			m = int(items[1])
			inData = True
			rowIndex = 0
			values = []
		else:
			rowIndex = rowIndex + 1
			templist = []
			for i in range(m):
				templist.append(int(items[i]))
			values.append(templist)
			
			if rowIndex == n:
				#print solve(currentCase, values)
				outFile.write(solve(currentCase, values))
				inData = False
				rowIndex = 0
				values = []
				currentCase = currentCase + 1
				if currentCase > totalCase:
					break

		
