T = int(raw_input())

def didIWonAgainstJ(teams,i,j):
	return teams[i][j] == "1"

def computeWpAndOpponents(N,teams):
	wp=[]
	opponentsA = []
	wins=[]
	
	for i,team in enumerate(teams):
		gamesCount = 0
		opponents = []
		winsCount = 0
		for j,c in enumerate(team):
			if c == "0":
				gamesCount+=1
				opponents.append(j)
			elif c== "1":
				winsCount+=1
				gamesCount+=1
				opponents.append(j)
		wp.append(float(winsCount)/gamesCount)
		opponentsA.append(opponents)
		wins.append(winsCount)
	return wp, opponentsA,wins
	
def computeOWP(teams,wp,opponents,wins):
	owp = []
	for i in range(len(teams)):
		sum = 0
		for j in opponents[i]:
			if didIWonAgainstJ(teams,j,i):
				sum += (wins[j]-1)/float(len(opponents[j])-1)
			else:
				sum += (wins[j])/float(len(opponents[j])-1)
		owp.append(sum/len(opponents[i]))
	return owp
	
def computeOOWP(teams,owp,opponents):
	oowp = []
	for i in range(len(teams)):
		sum = 0
		for j in opponents[i]:
			sum += owp[j]
		oowp.append(float(sum/len(opponents[i])))
	return oowp
		

def solveCase(t,N,teams):
	wp,opponents,wins = computeWpAndOpponents(N,teams)
	owp = computeOWP(teams,wp,opponents,wins)
	oowp = computeOOWP(teams,owp,opponents)
	#print "Wp : %s " % (wp)
	#print "Opponents : %s " % (opponents)
	#print "OWP : %s" % (owp)
	#print "OOWP : %s" % (oowp)
	print "Case #%d:" % (t)
	for i in range(len(teams)):
		print 0.25 *wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
	
		
for t in range(1,T+1):
	N = int(raw_input())
	teams = []
	for n in range(N):
		teams.append(raw_input())
	solveCase(t,N,teams)