#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case,values):
	
	bNotFull = False

	# â°4
	for i in range(4):
		judge = checkLine(values[i])
		if judge == "X" or judge == "O":
			return "Case #%d: %s won" % (case, judge) 
		elif judge == "NOTYET":
			bNotFull = True

	# èc4
	tempList = []
	for i in range(4):
		for j in range(4): 
			tempList.append(values[j][i])
		judge = checkLine(tempList)
		if judge == "X" or judge == "O":
			return "Case #%d: %s won" % (case, judge) 
		elif judge == "NOTYET":
			bNotFull = True
		tempList = []
	
	# éŒ1
	tempList = []		
	tempList.append(values[0][0])
	tempList.append(values[1][1])
	tempList.append(values[2][2])
	tempList.append(values[3][3])
	judge = checkLine(tempList)
	if judge == "X" or judge == "O":
		return "Case #%d: %s won" % (case, judge) 
	elif judge == "NOTYET":
		bNotFull = True

	# éŒ2
	tempList = []		
	tempList.append(values[3][0])
	tempList.append(values[2][1])
	tempList.append(values[1][2])
	tempList.append(values[0][3])
	judge = checkLine(tempList)
	if judge == "X" or judge == "O":
		return "Case #%d: %s won" % (case, judge) 
	elif judge == "NOTYET":
		bNotFull = True
	
	if bNotFull == True:
		return "Case #%d: Game has not completed" % case 
	else:
		return "Case #%d: Draw" % case 
	
def checkLine(buf):

	#print buf
	for i in range(len(buf)):
		if buf[i] == ".":
			return "NOTYET"

	status = "NONE"
	for i in range(len(buf)):
		v = buf[i]
		if v == ".":
			status = "NONE"
			break
		elif v == "X":
			if status == "NONE" or status == "X":
				status = "X"
			else:
				status = "NONE"
				break
		elif v == "O":
			if status == "NONE" or status == "O":
				status = "O"
			else:
				status = "NONE"
				break
			pass
	#print status
	return status


if __name__ == "__main__":
	values = [[0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0]]
	isFirst = True
	totalCase = 0
	currentCase = 1 
	rowIndex = 0

	for line in inFile.readlines():
		# first Line
		if isFirst == True:
			isFirst = False
			items = line.split()
			totalCase = int(items[0])
			continue

		# skip blank line
		if len(line) < 4:
			#print "next"
			continue
		
		# read all data
		if currentCase > totalCase:
				#print "break loop"
				break
        
		#get value
		for colIndex in range(0,4):
			values[rowIndex][colIndex] = line[colIndex]
		if rowIndex == 3:
			#print solve(currentCase, values)
			outFile.write(solve(currentCase, values) + "\n")
			rowIndex = 0
			if currentCase == totalCase:
				break
			else:
				currentCase = currentCase + 1
		else:
			rowIndex = rowIndex + 1


