import sys
lines = sys.stdin.readlines()

def calc_WP(games, team, ignore=None):
	total=0
	win=0

	for i in range(len(games[team])):
		score = games[team][i]
		if i!=ignore:
			if score=='0':
				total+=1
			if score=='1':
				win+=1
				total+=1
	
	return float(win)/total

def calc_OWP(games, team):
#	print "throwing games played agains team", team
	sum_IWPs = 0
	count=0
	for t in range(len(games)):
		if t!=team and games[t][team]!='.':
			IWP = calc_WP(games, t, team)
#			print "IWP(",t,"):",IWP
			sum_IWPs += IWP
			count+=1

	return float(sum_IWPs)/count

def calc_OOWP(games, OWPs, team):
	_sum=0
	count=0
	for t in range(len(games)):
		owp=OWPs[t]
		if t!=team and games[t][team]!='.':
			_sum += owp
			count+=1

	return float(_sum)/count


numcases = int(lines.pop(0))

for i in range(numcases):
		print "Case #"+str(i+1)+":"

		numteams = int(lines.pop(0))
		games = []
		for team in range(numteams):
			games.append(lines.pop(0))

		WPs=[]
		OWPs=[]
		OOWPs=[]

		for team in range(numteams):
			WPs.append(calc_WP(games, team))
#		print "WPs", WPs

		for team in range(numteams):
			OWPs.append(calc_OWP(games, team))
#		print "OWPs", OWPs

		for team in range(numteams):
			OOWPs.append(calc_OOWP(games, OWPs, team))
#		print "OOWPs", OOWPs

		for team in range(numteams):
			print 0.25 * WPs[team] + 0.5 * OWPs[team] + 0.25 * OOWPs[team]


