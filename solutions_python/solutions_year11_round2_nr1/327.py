from collections import defaultdict

def test_cases():
	from sys import stdin
	
	cases = int(stdin.readline())
	for i in xrange(cases):
		team_count = int(stdin.readline())
		games = defaultdict(lambda:None)
		blah = defaultdict(dict)
		games_played = defaultdict(lambda:0)
		for team in xrange(team_count):
			opponents = stdin.readline().strip()
			for opp in xrange(len(opponents)):
				if opponents[opp] != '.':
					blah[team][opp] = opponents[opp] == '1'
					games[(team, opp)] = opponents[opp] == '1'
					games_played[team] += 1
		yield (team_count, games, blah, games_played)

for (case_number, (team_count, games, games_by_team, games_played)) in enumerate(test_cases()):
	wp = {}
	for i in xrange(team_count):
		wp[i] = float(sum(games_by_team[i].values()))/games_played[i]
	
	owp = {}
	for me in xrange(team_count):
		opp_wps = {}
		for them in xrange(team_count):
			if me==them: continue
			result = games[(me, them)]

			if result is None:
				continue
			elif games_played[them] == 1:
				opp_wps[them] = 0
			else:
				opp_wps[them] = float(sum(games_by_team[them].values()) - int(not(result)))/(games_played[them]-1)
		owp[me] = sum(opp_wps.values())/len(opp_wps)
	
	oowp = {}
	for i in xrange(team_count):
		opponents = list(t[1] for t in owp.items() if t[0]!=i and games[(i,t[0])] is not None)
		oowp[i] = sum(opponents)/len(opponents)

	rpi = {}
	for i in xrange(team_count):
		rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
		
	
	print "Case #%d:" % (case_number+1)
	for i in xrange(team_count):
		print rpi[i]
