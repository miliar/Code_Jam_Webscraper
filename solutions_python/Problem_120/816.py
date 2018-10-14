#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case,rad,paint):
    used = 0
    currentRad = rad
    ringNum = 0

    isFirst = True
    base = 0

    while True:
        # ok but slow...
        #used += (currentRad + 1) * (currentRad +1) - currentRad * currentRad  
        used += 2*currentRad+1
        #if isFirst == True:
        #    base += 2*currentRad+1
        #    isFirst = False
        #    used = base
        #else:
        #    used += 4
        #print used
        if used > paint:
            break
        currentRad += 2
        ringNum += 1
    
    return "Case #%d: %d\n" % (case,ringNum) 

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
		
		rad = int(items[0])
		paint = int(items[1])

		#print solve(currentCase, rad, paint)
		outFile.write(solve(currentCase, rad, paint))
		currentCase = currentCase + 1
		if currentCase > totalCase:
			break

		
