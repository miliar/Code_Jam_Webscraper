import sys
from copy import copy

def insertPlate(plates, plate):
	for i in range(len(plates)):
		if(plate>plates[i]):
			plates.insert(i,plate)
			return

	plates.append(plate)
	return

def solvePancakes(sortedPlates, memoize):
	platesTuple = tuple(sortedPlates)

	if(memoize.get(platesTuple,None) != None):
		return memoize.get(platesTuple)

	else:
		biggestPlate = sortedPlates.pop(0)

		if(biggestPlate<4):
			return biggestPlate

		halfLine = biggestPlate//2
		minSoFar = biggestPlate

		for i in range(1,halfLine+1):
			newPlates = copy(sortedPlates)
			insertPlate(newPlates,i)
			insertPlate(newPlates,biggestPlate-i)

			subResult = solvePancakes(newPlates,memoize)
			minSoFar = min(minSoFar, 1 + subResult)

		memoize[platesTuple] = minSoFar
		return minSoFar

if __name__ == "__main__":
	ipfile = '/Users/amit/Downloads/B-small-attempt4.in'
	opfile = '/Users/amit/Downloads/output.txt'
	memoize = {}

	filestring = ''
	with open(ipfile,'r') as ipfile:
		cases = int(ipfile.readline())
		for case in range(1,cases+1):
			filledPlates = int(ipfile.readline())
			plates = ipfile.readline().split(' ')
			sortedPlates = sorted([int(i) for i in plates], reverse = True)

			answer = solvePancakes(sortedPlates, memoize)
			filestring = filestring + "Case #{0}: {1}\n".format(case, answer)

	print filestring
	with open(opfile,'w') as opfile:
		opfile.write(filestring)
