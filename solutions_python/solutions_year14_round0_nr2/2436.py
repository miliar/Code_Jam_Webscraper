def minTime(farmCost, farmRate, goal):
	numFarsm = 0
	totalTime = 0
	while True:
		currentRate = rate(numFarsm, farmRate)
		newFarmRate = rate(numFarsm + 1, farmRate)

		timeWithoutFarm = totalTime + time(currentRate, goal)
		timeWithFarm = totalTime + timeToFarm(currentRate, farmCost) + time(newFarmRate, goal)

		#print "timeWithoutFarm: {}".format(timeWithoutFarm)
		#print "timeWithFarm: {}".format(timeWithFarm)

		if timeWithoutFarm < timeWithFarm:
			return timeWithoutFarm

		totalTime += timeToFarm(currentRate, farmCost)
		numFarsm += 1

def rate(numFarsm, farmRate):
	return (2.0 + (numFarsm * farmRate))

def time(rate, goal):
	return (goal / rate)

def timeToFarm(rate, farmCost):
	return (farmCost / rate)

if __name__ == '__main__':
	numCases = int(raw_input())
	for case in xrange(numCases):
		vars = [float(var) for var in raw_input().split(" ")]
		farmCost = vars[0]
		farmRate = vars[1]
		goal = vars[2]

		print "Case #{}: {:0.7f}".format(case + 1, minTime(farmCost, farmRate, goal))