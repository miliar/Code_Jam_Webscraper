#!/usr/bin/env python
import sys

f = open(sys.argv[1]).readlines()
count = 0
totalRecords = int(f[0])
linesPerRecord = (len(f)-1)/totalRecords
data = []
#print linesPerRecord
for i in range(totalRecords):
	dataLine = []
	for j in range(linesPerRecord-1):
		#print i, totalRecords, j
		dataLine.append(list(f[(i*linesPerRecord)+j+1].strip()))
	#print dataLine
	data.append(dataLine)

case = 1

#Code starts here
def testLine(a,b,c,d):
	line = a+b+c+d
	#print line
	# Try for "O"
	test = line.replace("T","O")
	if test == "OOOO":
		return "O"
	# Try for "X"
	test = line.replace("T","X")
	if test == "XXXX":
		return "X"

	return None

f = open(sys.argv[1]+".out", "w")
for d in data:
	#print d
	lineFound = ""
	# Try Horizonal
	for i in range(4):
		retVal = testLine(d[i][0],d[i][1],d[i][2],d[i][3])
		if retVal != None:
			lineFound = retVal
			break
	
	# Try Vertical
	if lineFound == "":
		for i in range(4):
			retVal = testLine(d[0][i],d[1][i],d[2][i],d[3][i])
			if retVal != None:
				lineFound = retVal
				break
		
	# Try Diagonal
	if lineFound == "":
		retVal = testLine(d[0][0],d[1][1],d[2][2],d[3][3])
		if retVal != None:
			lineFound = retVal
		retVal = testLine(d[0][3],d[1][2],d[2][1],d[3][0])
		if retVal != None:
			lineFound = retVal

	# Print Results
	#print lineFound
	caseNum = "Case #"+str(case)+": "
	if lineFound == "O" or lineFound == "X":
		lineOut = caseNum+lineFound+" won"
	else:
		allSquares = ""
		for c in d:
			allSquares+="".join(c)
		#print allSquares
		if "." in allSquares:
			lineOut = caseNum+"Game has not completed"
		else:
			lineOut = caseNum+"Draw"
			
	print lineOut
	f.write(lineOut+"\n")
	
	case += 1
	
		
	
f.close()
