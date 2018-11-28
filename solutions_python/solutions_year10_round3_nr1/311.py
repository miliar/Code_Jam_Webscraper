#!/usr/bin/python
#  Developed by Rajiv Poplai 
import sys
#import pdb
#pdb.set_trace()


def findIntersections(newSrc, newDest, pointsList):
	intersection = 0
	for (src, dest) in pointsList:
		if (newSrc - newDest) == (src - dest):
			continue
		elif (newSrc -src) > 0 and (newDest - dest) > 0:
			continue
		elif (newSrc - src) < 0 and (newDest - dest) < 0:
			continue
		else:
			intersection += 1
	return intersection

def main():
	fileName = sys.argv[1]

	# Open input and output files
	inputFile = open(fileName, 'r')
	outputFile = open(fileName.strip('.in')+'.out', 'w')

	testCases = int(inputFile.readline().strip())
	for i in xrange(testCases):
		numberOfLines = int(inputFile.readline().strip())
		pointsList = [map(int, inputFile.readline().strip().split())]
		intersections = 0
		for j in xrange(numberOfLines-1):
			(newSrc, newDest) = map(int, inputFile.readline().strip().split())
			intersections = intersections + findIntersections(newSrc, newDest, pointsList) 
			pointsList.append((newSrc, newDest))
		outputFile.write('Case #'+str(i+1)+': '+str(intersections) + '\n')
	    

	# Close input and output files
	inputFile.close()
	outputFile.close()

if __name__ == "__main__":
	main()
