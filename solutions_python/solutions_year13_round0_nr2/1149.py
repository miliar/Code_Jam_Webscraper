#!/usr/bin/python

###### SET TO FALSE BEFORE SUBMIT ############################
debugOutput = False
##############################################################

maxTestCases = 0
lawnLength = -1
lawnWidth = -1

maxTestCases = int(raw_input().strip())

if debugOutput:
	print maxTestCases

for testCase in xrange(1, maxTestCases +1):
	answer = "NO"
	origLawn = list()
	newLawn = list()

	maxRows, maxCols = map(int, raw_input().strip().split())

	maxRowList = list()
	maxColList = list()

	if debugOutput:
		print maxRows, maxCols

	for r in xrange(0, maxRows):
		origLawn.append(map(int, raw_input().strip().split()))
		maxHeight = max(origLawn[r])
		newLawn.append([maxHeight] * maxCols)

	for c in xrange(0, maxCols):
		maxHeight = max(map(lambda x: origLawn[x][c], xrange(0, maxRows)))
		for r in xrange(0, maxRows):
			newLawn[r][c] = min(maxHeight, newLawn[r][c])

	if debugOutput:		
		for r in xrange(0, maxRows):
			for c in xrange(0, maxCols):
				#print origLawn[r][c], 
				print newLawn[r][c], 
			print

	if newLawn == origLawn:
		answer = "YES"

	print "Case #{}: {}".format(testCase, answer)
