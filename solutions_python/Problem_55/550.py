#!/usr/ybin/python
# themePark.py
# 08-May-2010
# Developed by Rajiv Poplai

import sys

	
def initTestCase(inputFile):
	line = inputFile.readline().strip()
	arr = line.split()
	R = int(arr[0])
	k = int(arr[1])
	n = int(arr[2])
	line = inputFile.readline().strip()
	arr = line.split()
	groups = []
	for i in xrange(n):
		groups.append(int(arr[i]))
	return (R, k, n, groups)

def runTestCase(inputFile):
	# R is number of rides
	# k is the capacity of roller coaster
	# n is the number of groups
	# groups is array containing number of members in the group
	(R, k, n, groups) = initTestCase(inputFile)
	print R, k, n, groups
	from collections import deque
	queue = deque(groups)
	earnings = 0
	for roundNum in xrange(R):
		emptySeats = k
		waitingQ = []
		while (len(queue) > 0 and queue[0] <= emptySeats):
			earnings = earnings + queue[0]
			emptySeats = emptySeats - queue[0]
			waitingQ.append(queue.popleft())
		# After the round is finished only then people who were in the ride get into the queue
		for i in waitingQ:
			queue.append(i)
	return earnings

def main():
	fileName = sys.argv[1]
	smallOrLarge = sys.argv[2]

	if (smallOrLarge == 'small'):
		maxR = 1000	# Max num of rides
		maxK = 100	# Max capacity of roller coaster
		maxN = 10	# Max num of groups

	inputFile = open(fileName, 'r')
	outputFile = open(fileName.strip('.in')+'.out', 'w')

	numOfTestCases = int(inputFile.readline().strip())
	print numOfTestCases

	for i in xrange(numOfTestCases):
		earnings = runTestCase(inputFile)
		outputFile.write('Case #'+str(i+1)+': '+str(earnings))
		if not (i+1 == numOfTestCases):
			outputFile.write('\n')
	inputFile.close()
	outputFile.close()



if __name__ == "__main__":
	main()
