from __future__ import print_function
import fileinput
import math

inputs = fileinput.input();
numCases = int(inputs[0]);
for q in range(0,numCases):
	numNonEmpty = int(inputs[q*2+1]);
	numOnPlates = inputs[q*2+2].split(' ');
	numOnPlates = [int(i) for i in numOnPlates];

	maxNum = max(numOnPlates);
	bestTime = maxNum;
	for curNum in range(1,maxNum):
		numSpecials = 0;
		numToCheck = [i for i in numOnPlates if i> curNum];
		for n in numToCheck:
			numDivides = math.ceil(float(n)/float(curNum))-1;
			numSpecials += numDivides;
		if numSpecials + curNum < bestTime:
			bestTime = numSpecials + curNum;
	bestTime = int(bestTime);
	print("Case #", q+1, ": ", bestTime, sep='');