#!/usr/bin/python
import sys

def theme_park():
	inputLines = sys.stdin.readlines()
	T = int(inputLines[0])
	
	for i in xrange(1,T+1):
		(R,k,N) = [int(val) for val in inputLines[i*2 - 1].split()]
		groupList = [int(val) for val in inputLines[i*2].split()]
		j = 1
		totalSum = 0
		while j <= R:
			seatList = []
			leftK = k
			j += 1
			while len(groupList) > 0 and groupList[0] <= leftK:
				totalSum += groupList[0]
				leftK -= groupList[0]
				seatList.append(groupList.pop(0))
			groupList.extend(seatList)
		print "Case #%d: %d" %(i, totalSum)

if "__main__" == __name__:
	theme_park()
