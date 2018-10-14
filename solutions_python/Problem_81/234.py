from __future__ import division
def wp(a, i):
	# win % of team i (0 indexed) from matrix a
	wins = 0
	games = 0
	for j in a[i]:
		if j == '1':
			wins += 1
			games += 1
		if j == '0':
			games += 1
	return wins/games
	
def owp(a, i):
	# win % on avg of all other enemy teams ignoring column i
	tw = []
	for t in range(len(a[i])):
		if a[i][t] != '.':
			wins = 0
			games = 0
			for _i in range(len(a[t])):
				if _i != i:
					if a[t][_i] == '1':
						wins += 1
						games += 1
					if a[t][_i] == '0':
						games += 1
			tw.append(wins/games)
	return sum(tw)/len(tw)

def oowp(a, i):
	# owp % on avg of all enemy teams
	ta = []
	for t in range(len(a[i])):
		if a[i][t] != '.':
			ta.append(owp(a, t))
	return sum(ta)/len(ta)

def rpi(a, i):
	return 0.25 * wp(a, i) + 0.5 * owp(a, i) + 0.25 * oowp(a, i)
	
f = open("A.in")
t = int(f.readline())
for _t in range(t):
	n = int(f.readline())
	m = []
	for _n in range(n):
		m.append(list(f.readline()[:-1]))
	print "Case #{0}:".format(_t+1)
	for _n in range(n):
		print rpi(m, _n)
