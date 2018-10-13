import sys

data = [x.strip() for x in open(sys.argv[1])]

T = int(data.pop(0))
out = open("out.txt", 'w')	
for t in xrange(T):
	out.write("Case #%d:\n" % (t+1))
	N = int(data.pop(0))
	wins = {}
	games = {}
	opponents = {}
	for n in xrange(N):
		results = data.pop(0)
		for opponent in xrange(n, N):
			result = results[opponent]
			if result == '.':
				pass
			else:
				try:
					opponents[n].append(opponent)				
				except KeyError:
					opponents[n] = [opponent]
				try:
					opponents[opponent].append(n)
				except KeyError:
					opponents[opponent] = [n]
				try:
					games[n] += 1
				except KeyError:
					games[n] = 1.0
				try:
					games[opponent] += 1
				except KeyError:
					games[opponent] = 1.0
				if result == '1':
					try:
						wins[n].append(opponent)
					except KeyError:
						wins[n] = [opponent]
				else:
					try:
						wins[opponent].append(n)
					except KeyError:
						wins[opponent] = [n]
	WP = {}
	OWP = {}
	for n in xrange(N):
		if n in wins:
			WP[n] = len(wins[n]) / games[n]
		else:
			WP[n] = 0.0
		opp_wins = []
		OWP[n] = 0.0
		for opponent in opponents[n]:
			if opponent in wins:
				if n in wins[opponent]:
					OWP[n] += (len(wins[opponent])-1) / (games[opponent]-1)
				else:
					OWP[n] += len(wins[opponent]) / (games[opponent]-1)
		OWP[n] = OWP[n] / games[n]
	
	for n in xrange(N):
		OOWP = 0.0
		for opponent in opponents[n]:
			OOWP += OWP[opponent]
		OOWP = OOWP / games[n]
		RPI = 0.25 * WP[n] + 0.50 * OWP[n] + 0.25 * OOWP
		out.write("%f\n" % RPI)
out.close()
		