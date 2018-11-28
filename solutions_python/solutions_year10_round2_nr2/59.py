T = int(raw_input())

for CASE in xrange(1,T+1):
	(N,K,B,T) = map(int, raw_input().split(' '))

	X =  map(int, raw_input().split(' '))
	V =  map(int, raw_input().split(' '))

	fails = 0
	wins = 0
	swaps = 0
	for k in range(N-1,-1,-1):
		if X[k]+V[k]*T >= B:
			wins = wins + 1
			swaps += fails
		else:
			fails = fails+1
		if wins == K: break

	if wins == K: print 'Case #'+str(CASE)+': '+str(swaps)
	else:print 'Case #'+str(CASE)+': IMPOSSIBLE'




