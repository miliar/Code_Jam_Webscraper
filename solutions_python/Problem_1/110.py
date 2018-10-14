input  = file("A-large.in")
totalNumber = int(input.readline())
for n in range(totalNumber):
	numberOfEngines = int(input.readline())
	for engine in range(numberOfEngines):input.readline()
	numberOfQueries = int(input.readline())
	queries = []
	for querie in range(numberOfQueries):queries += [input.readline()]
	enginesSoFar = []
	swaps = 0
	for querie in queries:
		if querie not in enginesSoFar:
			enginesSoFar += [querie]
		if  len(enginesSoFar) == numberOfEngines:
			swaps += 1
			enginesSoFar = [querie]
	print 'Case #%i: %i' %(n+1,swaps)
