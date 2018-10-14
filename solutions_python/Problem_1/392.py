import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

totalTrials = int(input.readline())
trialsCompleted = 0

def findOptimalSwitches(engineDict, searches, trialNum):
	numEngines = len(engineDict.keys())
	numSearches = len(searches)
	currentEngine = getFurthestAway(searches, engineDict.keys(), None)
	currentUses = {}
	switches = 0
	n = 0
	while n < numSearches:
		if searches[n] == currentEngine:
			currentEngine = getFurthestAway(searches[n+1:], engineDict.keys(), currentEngine)
			switches += 1
		n += 1
	return "Case #%d: %d" % (trialNum, switches)

def getFurthestAway(l, engineList, currentEngine):
	''' A greedy algorithm to pick the engine used furthest in the future '''
	enginesUsed = {}
	if currentEngine:
		enginesUsed[currentEngine] = True
	numEngines = len(engineList)
	for engine in l:
		enginesUsed[engine] = True
		if len(enginesUsed.keys()) == numEngines:
			return engine
	n = 0
	while n < numEngines:
		if engineList[n] not in enginesUsed.keys():
			return engineList[n]
		n += 1
	sys.exit(1)

while trialsCompleted < totalTrials:
	trialsCompleted += 1
	numEngines = int(input.readline())
	searchEngines = {}
	n = 0
	while n < numEngines:
		searchEngines[input.readline()[:-1]] = True
		n += 1
	n = 0
	numSearches = int(input.readline())
	searches = []
	while n < numSearches:
		searches.append(input.readline()[:-1])
		n += 1
	
	s = findOptimalSwitches(searchEngines, searches, trialsCompleted)
	output.write("%s\n" % s)

input.close()
output.close()

