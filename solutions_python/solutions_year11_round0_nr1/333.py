
file = open("A-large.in")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])

for nCase in range(1, nCases + 1):
	aChTokens = aStrLines[nCase].split()
	aChTokens = aChTokens[1:]
	
	dictTimes = dict(B=1, O=1)
	dictLocs = dict(B=1, O=1)
	timeCur = 1
	
	while len(aChTokens) > 0:
		botCur = aChTokens[0]
		nButton = int(aChTokens[1])
		aChTokens = aChTokens[2:]
		
		timeBot = dictTimes[botCur] + abs(dictLocs[botCur] - nButton)
		timeNext = max(timeCur, timeBot) + 1
		dictTimes[botCur] = timeNext
		dictLocs[botCur] = nButton
		timeCur = timeNext
		
	print "Case #" + str(nCase) + ": " + str(timeCur - 1)
	
	