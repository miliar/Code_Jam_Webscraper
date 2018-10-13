#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	n = int(raw_input())
	A = []
	for i in xrange(n):
		A.append(raw_input())
	WP = []
	OWP = []
	OOWP = []
	for i in xrange(n):
		games = 0
		wins = 0
		for j in xrange(n):
			if A[i][j] != '.':
				games += 1
			if A[i][j] == '1':
				wins += 1
		WP.append(wins * 1.0 / games)

	for i in xrange(n):
		total_sum = 0
		count = 0
		for j in xrange(n):
			if A[i][j] == '.':
				continue
			games = 0
			wins = 0
			for l in xrange(n):
				if l == i:
					continue
				if A[j][l] != '.':
					games += 1
				if A[j][l] == '1':
					wins += 1
			total_sum += wins * 1.0 / games
			count += 1

		OWP.append(total_sum * 1.0 / count)

	for i in xrange(n):
		total_sum = 0
		count = 0
		for j in xrange(n):
			if A[i][j] == '.':
				continue
			total_sum += OWP[j]
			count += 1
		OOWP.append(total_sum * 1.0 / count)
	
	print "Case #%d:" % (t + 1)
	for i in xrange(n):
		#print WP[i], OWP[i], OOWP[i]
		print 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]

