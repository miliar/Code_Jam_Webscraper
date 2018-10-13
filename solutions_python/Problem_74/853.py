#!/bin/python
import sys

fileName = sys.argv[1]

inputFile = open(fileName, 'r')
outputFile = open(fileName.strip('.in')+'.out', 'w')

numOfTestCases = int(inputFile.readline().strip())
for i in xrange(numOfTestCases):
	line = inputFile.readline().strip()
	arr = line.split()
	totalNumberOfMoves = int(arr[0])
	curPosition = {'O':1, 'B':1}
	moveMap = []
	currentTarget = 0
	nextMove = { 'O': [], 'B': [] }
	for move in xrange(totalNumberOfMoves):	
		roboName = arr[move*2+1]
		roboPos = int(arr[move*2 + 2])
		moveMap.append(( roboName, roboPos))
		nextMove[roboName].append(roboPos)
	t = 1
	while (1) :
		buttonPressed = False
		#print 'At time t = ',t
		for robot in curPosition.keys():
			if (nextMove[robot] == []):
				#print '---%s Stay at button %s' % (robot, str(curPosition[robot]))
				pass
			elif (curPosition[robot] < nextMove[robot][0]):
				curPosition[robot] = curPosition[robot] + 1
				#print '---%s Move to button %s' % (robot, str(curPosition[robot]))
			elif (curPosition[robot] > nextMove[robot][0]):
				curPosition[robot] = curPosition[robot] - 1
				#print '---%s Move to button %s' % (robot, str(curPosition[robot]))
			elif (moveMap[currentTarget][0] == robot):
				#print '---%s Push button %s' % (robot, str(curPosition[robot]))
				buttonPressed = True
				del nextMove[robot][0]
			else:
				#print '---%s Stay at button %s' % (robot, str(curPosition[robot]))
				pass
		if (buttonPressed):
			currentTarget = currentTarget + 1
		if (currentTarget == totalNumberOfMoves):
			break
		t = t + 1			
	outputFile.write('Case #'+str(i+1)+': '+str(t))
	if i != (numOfTestCases - 1):
		outputFile.write('\n')
inputFile.close()
outputFile.close()