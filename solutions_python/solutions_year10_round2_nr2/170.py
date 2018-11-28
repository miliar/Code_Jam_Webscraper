#!/usr/bin/python2.6
import sys
data = sys.stdin
caseno = int(data.readline())
for case in xrange(1,caseno+1):
	print "Case #%d:"%case,
	possible = True
	N, K, B, T = map(int,data.readline().split())
	X = map(int,data.readline().split())
	V = map(int,data.readline().split())
	order = []
	finish = []
	madeit = 0
	for i in xrange(N):
		if X[i] + V[i]*T >= B:
			madeit+=1
			finish.append(i)

		order.append(i)
	order.sort()
	order.reverse()
	finish.sort()
	finish.reverse()
	finish = finish[:K]

	if madeit < K:
		possible = False
	swap = 0	
	if possible:
		madeit = 0
		for i in xrange(N-1):
			if X[order[i]] + V[order[i]]*T >= B:
				madeit += 1

			if X[order[i]] + V[order[i]]*T < B:
				for j in xrange(len(finish)):
					if X[finish[j]] < X[order[i]]:
						swap += 1
					

				
	
	if not possible:
		print 'IMPOSSIBLE'
	else:
		print swap 
