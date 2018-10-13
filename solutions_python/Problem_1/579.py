def parseInput(inFile):
	lines = [r.strip() for r in file(inFile,"rb").readlines()]
	# read the number of test cases:
	testCasesNum = int(lines[0])
	testCases = []
	lines = lines[1:]
	currentIndex = 0
	for i in range(testCasesNum):
		searchEngines = []
		for j in range(int(lines[currentIndex])):
			searchEngines.append(lines[currentIndex+1+j])
		currentIndex = currentIndex + 1 + int(lines[currentIndex])
		queries = []
		for j in range(int(lines[currentIndex])):
			queries.append(lines[currentIndex+1+j])
		currentIndex = currentIndex + 1 + int(lines[currentIndex])
		testCases.append((searchEngines, queries))
	return testCases

# The algorithm, is a greedy one.Go to the list of queries, and erase for each query the search engine it apears in.
# when we go to zero, we switch.
def getNumberOfSwitches(searchEngines,queries):
	numberOfSwitches = 0
	copiedSearchEngoneList = list(searchEngines)
	for q in queries:
		if q in copiedSearchEngoneList:
			# now we must make a switch. O dear!
			if len(copiedSearchEngoneList) == 1:
				numberOfSwitches += 1
				copiedSearchEngoneList = list(searchEngines)
			# We need to remove the current engine either case, as we can't switch to it.
			copiedSearchEngoneList.remove(q)
	return numberOfSwitches



# parse input:
cases = parseInput("input")
i = 1
for c in cases:
	print "Case #%d: %d" % (i, getNumberOfSwitches(*c))
	i += 1

