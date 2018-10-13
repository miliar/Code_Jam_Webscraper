#!/usr/bin/python

import sys

def getWP(games, teams):
	wp = []
	# print("games = %s" % str(games))
	for a in teams:
		wins = 0
		numGames = 0
		for b in teams:
			if (a,b) in games:
				wins += games[ (a,b) ]
				numGames += 1
				
		# print("a = %d" % a)
		# print("wp = %f" % (float(wins) / float(numGames)))
		wp.append(float(wins) / float(numGames))
	return wp

def mean(a):
	return sum(a) / float(len(a))

def solve(numTeams, games):
	teams = [i for i in range(0, numTeams)]
	wp = getWP(games, teams)
	# print("wp = %s" % str(wp))
	owp = []
	for i in range(0, numTeams):
		gamesi = dict(games)
		for a in range(0, numTeams):
			if (a,i) in gamesi:
				gamesi.pop( (a,i) )
			if (i,a) in gamesi:
				gamesi.pop( (i,a) )
		_teams = teams[:]
		_teams.remove(i)
		# print("i = %d" % i)
		# print("_teams = %s" % str(_teams))
		wps = getWP(gamesi, _teams)
		for a in reversed(range(0, numTeams)):
			if (a,i) not in games and (i,a) not in games and a in _teams:
				wps.pop(_teams.index(a))
		owp.append( mean(wps) )

	# print("owp = %s" % str(owp))

	oowp = []
	for i in range(0, numTeams):
		_owp = []
		for a in range(0, numTeams):
			if (a,i) in games or (i,a) in games:
				_owp.append(owp[a])
		oowp.append(mean(_owp))
	# print("oowp = %s" % str(oowp))

	r = "\n"
	for i in range(0, numTeams):
		rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
		r += str(rpi)
		if i+1 < numTeams:
			r += "\n"
	return r

f = open(sys.argv[1], 'r')
for c in range(1, int(f.readline())+1):
	numTeams = int(f.readline())
	games = dict()
	wins = [0 for x in range(0, numTeams)]
	totalGames = [0 for x in range(0, numTeams)]
	for a in range(0, numTeams):
		line = f.readline().strip()
		for b in range(0, numTeams):
			if line[b] == '1':
				games[(a,b)] = 1
			elif line[b] == '0':
				games[(a,b)] = 0
	print("Case #%d: %s" % (c, solve(numTeams, games)))

