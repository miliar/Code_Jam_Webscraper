
file = open("A-large.in")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])
aStrLinesLeft = aStrLines[1:]

for nCase in range(1, nCases + 1):
	nTeams = int(aStrLinesLeft[0])
	aStrLinesCur = aStrLinesLeft[1:nTeams+1]
	aStrLinesLeft = aStrLinesLeft[nTeams+1:]
	
	lRWp = nTeams * [0]
	llITeamsPlayed = []
	i = 0
	
	for strTeam in aStrLinesCur:
		nWins = 0
		j = 0
		llITeamsPlayed.append([])
		for ch in strTeam:
			#print "Team " + str(i) + " played a game: " + ch
			if ch != '.':
				llITeamsPlayed[i].append(j)
			if ch == '1':
				nWins = nWins + 1
			j += 1
		#print "Team " + str(i) + " won " + str(nWins) + " out of " + str(len(llITeamsPlayed[i]))
		#print "The list: " + str(llITeamsPlayed)
		lRWp[i] = float(nWins) / len(llITeamsPlayed[i])
		i += 1
	
	lROwp = nTeams * [0]
	
	i = 0
	for lIPlayed in llITeamsPlayed:
		sum = 0.0
		for iPlayed in lIPlayed:
			gamesWon = lRWp[iPlayed] * len(llITeamsPlayed[iPlayed])
			if aStrLinesCur[i][iPlayed] == '0':
				gamesWon -= 1
			#print "Team " + str(i) + " played " + str(iPlayed) + ", who won " + str(gamesWon) + " other games"
			sum += gamesWon / (len(llITeamsPlayed[iPlayed]) - 1)
		
		lROwp[i] = sum / len(lIPlayed)
		i += 1
	
	lROowp = nTeams * [0]
	
	i = 0
	for lIPlayed in llITeamsPlayed:
		sum = 0.0
		for iPlayed in lIPlayed:
			sum += lROwp[iPlayed]
		
		lROowp[i] = sum / len(lIPlayed)
		i += 1
		
	print "Case #" + str(nCase) + ":"
	
	for i in range(nTeams):
		print str(0.25 * lRWp[i] + 0.5 * lROwp[i] + 0.25 * lROowp[i])
		#print "Components: " + str(lRWp[i]) + ", " + str(lROwp[i]) + ", " + str(lROowp[i])
