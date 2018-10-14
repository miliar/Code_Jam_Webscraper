#!/usr/bin/env python
import sys
import os
import string
import collections
import math

def totalReceipts(iRuns, iSeats, iNumberOfGroups, lstGroups):
	iMoneyForRun = []
	iNextStartingPosition = []
	iNextPosition = 0
	iRemainingRuns = iRuns
	iAccum = 0
	# Find where we start a pattern, has to be <= iNumberOfGroups 
	while iNextStartingPosition.count(iNextPosition) == 0 and len(iNextStartingPosition) < iRuns:
		iNextStartingPosition.append(iNextPosition)
	
		queGroups = collections.deque(lstGroups)
		queGroups.rotate(iNextPosition)
		iMoney = 0
		iAvailableSeats = iSeats
		while len(queGroups) > 0 and iAvailableSeats - queGroups[0] >= 0:
			iNextGroup = queGroups.popleft()
			iAccum = iAccum + 1
			iAvailableSeats = iAvailableSeats - iNextGroup
			iMoney = iMoney + iNextGroup

		iMoneyForRun.append(iMoney)

		iNextPosition = ((iNextPosition + len(queGroups)) % iNumberOfGroups) 

	iPatternStart = 0
	iDaysTotal = 0

	# If we complete the number of runs then just total up the reciepts
	if len(iNextStartingPosition) == iRuns:
		return sum(iMoneyForRun)
	

	iPatternStart = iNextStartingPosition.index(iNextPosition)
	# Money collected just before we start our pattern
	iDaysTotal = sum(iMoneyForRun[0:iPatternStart])
	# Number of Runs we complete before starting our pattern
	iRemainingRuns = iRemainingRuns - iPatternStart
	# How many times we have to loop through the pattern
	iNumberOfLoopsThroughPattern = math.floor(iRemainingRuns / len(iNextStartingPosition[iPatternStart:]))
	iDaysTotal = iDaysTotal + sum(iMoneyForRun[iNextStartingPosition.index(iNextPosition):]) * iNumberOfLoopsThroughPattern
	
	# Incase we dont make it completely through the pattern figure out how fare we get through that lsat time
	iRemainingRuns = iRemainingRuns - len(iNextStartingPosition[iPatternStart:]) * iNumberOfLoopsThroughPattern
	iLastIndex = int(iPatternStart + iRemainingRuns)
	iDaysTotal = iDaysTotal + sum(iMoneyForRun[iPatternStart:iLastIndex])
	return long(iDaysTotal)
		
def main():
	file = sys.argv[1]
	currentTestCase = 1
	with open(file) as f:
		testCaseCount = int(f.readline())
		for counter in range(testCaseCount):
			sTestLine = f.readline().strip()
			iR = int(sTestLine.split(' ')[0])
			ik = int(sTestLine.split(' ')[1])
			iN = int(sTestLine.split(' ')[2])
			
			sGroups = f.readline().strip()
			lstGroups = []
			for sGroupSize in sGroups.strip().split(' '):
				lstGroups.append(int(sGroupSize))
			print "Case #%(caseNumber)d: %(output)s" % {'caseNumber': counter + 1, 'output': totalReceipts(iR, ik, iN, lstGroups)}

if __name__ == "__main__":
	main()


