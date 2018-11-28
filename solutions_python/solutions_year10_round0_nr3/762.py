import psyco

sample = file("C-large.in", "rb")
output = file("output.out", "wb")

def solve(caseNumber, runCount, sizeOfTrain, numberOfGroups, groupsCount):
	euros = 0
	currentPosition = 0
	bestPacking = []

	# precalculation for each group
	for i in xrange(numberOfGroups):
		sum = 0
		gotMatch = False

		for j in xrange(numberOfGroups):
			currentGroup = (j + i) % numberOfGroups

			sum += groupsCount[currentGroup]
			
			if sum > sizeOfTrain:
				sum -= groupsCount[currentGroup]
				gotMatch = True
				break
		
		if gotMatch:
			bestPacking.append((sum, currentGroup))
		else:
			bestPacking.append((sum, i))
	
	for i in xrange(runCount):
		money, offsetPos = bestPacking[currentPosition]

		euros += money
		currentPosition = offsetPos
	
	print "Case #%d: %d" % (caseNumber, euros)
	output.write("Case #%d: %d\n" % (caseNumber, euros))

psyco.full()

numberOfTestCases = int(sample.readline())

for i in xrange(numberOfTestCases):
	R, k, N = sample.readline().split(" ")
	R = int(R)
	k = int(k)
	N = int(N)

	groupsCount = sample.readline().split(" ")
	groupsCount = [int(a) for a in groupsCount]

	solve(i + 1, R, k, N, groupsCount)