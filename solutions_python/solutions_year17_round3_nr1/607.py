import itertools 
from operator import itemgetter
import math

def findsubsets (S, m):
	return set (itertools.combinations(S, m))


def getSurfaceArea (sortedSet):
	area = 0
	for i, cylinder in enumerate (sortedSet):
		r = cylinder [0]
		h = cylinder [1]
		if i == 0:
			area += 2*math.pi*r*h + math.pi*r*r
		else:
			prevR = sortedSet [i-1][0]
			area += 2*math.pi*r*h + math.pi*(r*r-prevR*prevR)
	return area

def getMaxSurfaceArea (cylinders, needed):
	subsets = findsubsets (cylinders, needed)
	maxArea = -1;
	for subset in subsets:
		sortedSubset = tuple (sorted (subset, key=itemgetter(0)))
		curArea = getSurfaceArea (sortedSubset)
		if (curArea > maxArea):
			maxArea = curArea

	return maxArea

fRead = open ("A-small-attempt1.in", "r")
fWrite = open ("A-small-attempt1-output.txt", "w")

numTests = int (fRead.readline())

for i in range (numTests):
	pancakeInfo = fRead.readline()
	numPancakes, numNeeded = [int (x) for x in pancakeInfo.split()]
	panackes = []
	for j in range (numPancakes):
		curPanckakeInfo = tuple ([int (x) for x in fRead.readline().split()])
		panackes.append (curPanckakeInfo)
	maxArea = getMaxSurfaceArea (panackes, numNeeded)
	fWrite.write ("Case #" + str (i+1) + ": " + str (maxArea) + "\n")

fRead.close ()
fWrite.close ()
