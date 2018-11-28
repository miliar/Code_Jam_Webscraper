import re
import sys
import math

cases = list()
lineNumb = 0;
testCases = 0;

def outputSolution(solution):
	countSolution = 1;

	for s in solution:
		print "Case #"+str(countSolution)+": "+str(s[0])+" "+str(s[1]);
		countSolution = countSolution + 1


with open(sys.argv[1]) as file:
	for line in file:

		if(lineNumb == 0):
			testCases = int(line.strip())
		
		else:
			data = line.strip().split(" ")
			test = dict()
			test["N"] = int(data[0])
			test["K"] = int(data[1])
			cases.append(test)

		lineNumb = lineNumb + 1

def computeSolution(stalls):
	stalls = int(stalls)
	Max = stalls / 2
	Min = stalls / 2 - (stalls%2 == 0)

	return [Max, Min]

def solve(case):
	stalls = case['N']
	person = case['K']

	level = int(math.floor(math.log(person,2)))

	stallsAtLevel = stalls - 2**level + 1
	personAtLevel = person - 2**(level) + 1

	sectionSize = stallsAtLevel

	if level == 0:
		sectionSize = stallsAtLevel
	else:
		blockSize = int(stallsAtLevel / 2**(level-1))
		# bigSectionSize =  int(math.ceil(blockSize * 1.0 / 2))
		smallSectionSize = int(math.floor(blockSize * 1.0 / 2))
		bigSectionSize = smallSectionSize + 1

		sections = 2**level

		# smallSectionSizeCount = 

		# bigSectionSizeCount = 2 ** (level - 1)
		# smallSectionSizeCount = 2 ** (level - 1)

		# bigSectionSizeCount = (stallsAtLevel - (smallSectionSize * smallSectionSizeCount)) / smallSectionSize

		if smallSectionSize == 0:
			bigSectionSize = 1;
			smallSectionSize = 1;
			bigSectionSizeCount = 0
			smallSectionSizeCount = stallsAtLevel - bigSectionSizeCount
		else:
			smallSectionSizeCount = (stallsAtLevel - (bigSectionSize * sections)) / (smallSectionSize - bigSectionSize);
			assert(int(smallSectionSizeCount) == smallSectionSizeCount)
			bigSectionSizeCount = sections - smallSectionSizeCount;


		totalStalls = bigSectionSizeCount * bigSectionSize + smallSectionSizeCount * smallSectionSize

		# print "\t".join(map(str,[stalls, level, stallsAtLevel, bigSectionSize, bigSectionSizeCount, smallSectionSize, smallSectionSizeCount, personAtLevel]))
		assert(totalStalls == stallsAtLevel)

		if personAtLevel <= bigSectionSizeCount:
			sectionSize = bigSectionSize
		else:
			sectionSize = smallSectionSize
		
	[Max, Min] = computeSolution(sectionSize);

	# print "\t".join(map(str,[stalls, person, level, stallsAtLevel, sectionSize]))

	return [Max, Min]


solution = []

# print cases

for c in cases:
	solution.append(solve(c));

outputSolution(solution)