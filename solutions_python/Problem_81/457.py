'''
Created on May 21, 2011

@author: Nathan V-C
'''


def parseLine(testLine):
	return list(testLine.replace('\n', ''))

def getFinalList(games):
	WP = []
	OWP = []
	OOWP = []
	
	numPlayers = len(games)
	
	for playerGames in games:
		won = 0.0
		totalPlayed = 0.0
		for game in playerGames:
			if game == '1':
				won += 1
				totalPlayed += 1
			elif game == '0':
				totalPlayed += 1
		
		WP.append(won / totalPlayed)
		
	for playerNum in range(numPlayers):
		playerGames = games[playerNum]
		
		totalOW = 0.0
		numOpps = 0
		for oppNum in range(numPlayers):
			if games[oppNum][playerNum] != '.':
				oppGame = games[oppNum]
				won = 0.0
				totalPlayed = 0.0
				for oppGameNum in range(numPlayers):
					game = oppGame[oppGameNum]
					if oppGameNum != playerNum:
						if game == '1':
							won += 1
							totalPlayed += 1
						elif game == '0':
							totalPlayed += 1
				
				totalOW += won / totalPlayed
				numOpps += 1
		OWP.append(totalOW / numOpps)
	
	for playerNum in range(numPlayers):
		totalOWP = 0.0
		numOpps = 0
		for oppNum in range(numPlayers):
			if games[oppNum][playerNum] != '.':
				totalOWP += OWP[oppNum]
				numOpps += 1
		OOWP.append(totalOWP / numOpps)
	
	return WP, OWP, OOWP
						

def createOutStr(testNum, WP, OWP, OOWP):
	RPI = []
	for player in range(len(WP)):
		RPI.append(str(0.25 * WP[player] + 0.50 * OWP[player] + 0.25 * OOWP[player]))
		
	return 'Case #%i:\n%s' % (testNum, '\n'.join(RPI))

def main(fileNameIn, fileNameOut):
	fIn = open(fileNameIn)
	fOut = open(fileNameOut, 'w')
	numTests = int(fIn.readline())
	
	for testNum in range(1, numTests + 1):
		games = []
		numPlayers = int(fIn.readline())
		for player in range(numPlayers):
			games.append(parseLine(fIn.readline()))
			
		WP, OWP, OOWP = getFinalList(games)
		
		outStr = createOutStr(testNum, WP, OWP, OOWP)
		print outStr
		fOut.write(outStr + '\n')
	
	fIn.close()
	fOut.close()

main('A-large.in', 'out')