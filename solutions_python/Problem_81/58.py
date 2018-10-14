# -*- coding: utf-8 -*-


from collections import defaultdict as dd





T = int(raw_input())

for t in range(1,1+T):
	
	N = int(raw_input())
	
	result = dd(lambda:-1)
	
	for i in range(N):
		line = raw_input()
		for j in range(N):
			c = line[j]
			if c=='.':
				result[i,j] = -1
			else:
				result[i,j] = int(c)
	
	WP = {}
	for i in range(N):
		games = [result[i,j] for j in range(N)]
		wins = games.count(1)
		losses = games.count(0)
		WP[i] = float(wins)/float(wins+losses)
	#print 'WP'
	#print WP
	#print
	
	OWP = {}
	for i in range(N):
		total = 0.
		count = 0
		for j in range(N):
			if j==i: continue
			if result[i,j]==-1: continue
			games = [result[j,k] for k in range(N) if k!=i]
			wins = games.count(1)
			losses = games.count(0)
			wp = float(wins)/float(wins+losses)
			total += wp
			count += 1
		OWP[i] = total/count
	#print 'OWP'
	#print OWP
	#print
	
	OOWP = {}
	for i in range(N):
		total = 0.
		count = 0
		for j in range(N):
			if j==i: continue
			if result[i,j]==-1: continue
			total += OWP[j]
			count += 1
		OOWP[i] = total/count
	#print 'OOWP'
	#print OOWP
	#print
	
	RPI = [ 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i] for i in range(N) ]
	
	print 'Case #{x}:'.format(x=t)
	for rpi in RPI:
		print rpi
	

















