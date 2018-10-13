
T = int(raw_input())

for t in range(1, T+1):
	N = int(raw_input())
	ret = {}
	matrix = []
	
	for i in range(N):
		matrix.append(list(raw_input()))
	WP = {}
	OWP = {}
	
	for team in range(N):
		# compute WP
		n_wins = 0
		n_lost = 0
		for j in range(N):
			if matrix[team][j] == '1':
				n_wins += 1
			elif matrix[team][j] == '0':
				n_lost += 1
		WP[team] = float(n_wins) / (n_lost+n_wins) if n_lost+n_wins else 0.0
	
		# compute OWP
		s = 0.0
		i = 0
		l = []
		for o_team in range(N):
			if o_team != team and matrix[o_team][team] != '.':
				i += 1
				n_wins, n_lost = 0, 0
				for j in range(N):
					if j != team and j != o_team and matrix[o_team][j] == '1':
						n_wins += 1
					elif j != team and j != o_team and matrix[o_team][j] == '0':
						n_lost += 1
				s += float(n_wins) / (n_lost+n_wins) if n_lost+n_wins else 0.0
				l.append(float(n_wins) / (n_lost+n_wins) if n_lost+n_wins else 0.0)
		OWP[team] = s / i
	
	res = []
	for team in range(N):
		s = 0.0
		c = 0
		for r in range(N):
			if matrix[r][team] != '.':
				s += OWP[r]
				c += 1
		OOWP = s / c
		res.append(0.25 * WP[team] + 0.5 * OWP[team] + 0.25 * OOWP)
	print 'Case #%d:' % t
	for r in res:
		print r
