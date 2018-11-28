import psyco
import sys

INPUT_FILENAME = "B-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, numberOfChicks, minimalNumberOfChicks, barnLocation, timeLimit, locations, velocities):
	# find time to target
	timeToTarget = []
	for i in xrange(numberOfChicks):
		timeToTarget.append(float(barnLocation - locations[i]) / velocities[i])
	
	goodChicks = []
	
	for i in xrange(numberOfChicks):
		if timeToTarget[i] <= timeLimit:
			goodChicks.append(i)
	
	if len(goodChicks) < minimalNumberOfChicks:
		result = "IMPOSSIBLE"
	else:
		bestChicks = []
		tempLocations = locations[:]

		while tempLocations != [] and len(bestChicks) != minimalNumberOfChicks:
			index, value = max(enumerate(tempLocations), key = lambda x: x[1])
			if index in goodChicks:
				bestChicks.append(index)
		
			tempLocations = tempLocations[:index] + tempLocations[index + 1:]
		
		# cannot happend
		if len(bestChicks) != minimalNumberOfChicks:
			print "Bad"
			sys.exit()
		
		bestChicks.reverse()
		result = 0
		
		for j in xrange(minimalNumberOfChicks):
			firstLocation = locations[bestChicks[j]]
			firstVelocity = velocities[bestChicks[j]]

			for k in xrange(bestChicks[j] + 1, numberOfChicks):
				secondLocation = locations[k]
				secondVelocity = velocities[k]

				if firstVelocity == secondVelocity:
					continue
				
				t = float(firstLocation - secondLocation) / float(secondVelocity - firstVelocity)
				if t < 0 or t >= min(timeToTarget[bestChicks[j]], timeToTarget[k]):
					continue
				
				if firstLocation + firstVelocity * t + secondVelocity * (timeLimit - t) < barnLocation:
					result += 1

	toOutput("Case #%d: %s" % (caseNumber, result))

numberOfTestCases = int(sample.readline())

for i in xrange(numberOfTestCases):
	numberOfChicks, minimalNumberOfChicks, barnLocation, timeLimit = [int(num) for num in sample.readline().split(" ")]
	locations = [int(num) for num in sample.readline().split(" ")]
	velocities = [int(num) for num in sample.readline().split(" ")]

	solve(i + 1, numberOfChicks, minimalNumberOfChicks, barnLocation, timeLimit, locations, velocities)