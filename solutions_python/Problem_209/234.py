from math import pi

T = int(raw_input())

for test in xrange(1,T+1):
	N, K = map(int, raw_input().split())
	R = [] 
	for _ in xrange(N):
		r, h = map(int, raw_input().split())
		R.append((r,h))
	R.sort() 
	
	f = [ [0.]*(N+1) for _ in xrange(N+1)] 
	for i in xrange(N): f[i][0] = 2*R[i][0]*R[i][1]
	for i in xrange(1,N):
		for j in xrange(1,i+1): 
			f[i][j] = 2*R[i][0]*R[i][1] + max( f[k][j-1] for k in xrange(j-1, i))
	ans = pi*max( R[i][0]**2 + f[i][K-1] for i in xrange(K-1, N))	
	print "Case #%d: %.7f"%(test, ans)
 
