from sys import *

def solve(i, X, V, K, B, T):
	
	if K==0:
		print "Case #%d: %s" %(i+1, 0)
		return
	
	D = map(lambda x: B-x, X)
	Ts = map(lambda x,y: (float)(x)/(float)(y), D, V)
	
	goal = 0
	n_swaps = 0
	prev = 0
	for j in xrange(1, len(X)+1):
		if goal >= K:
			break
		if Ts[-j] <= T:
			goal += 1
			n_swaps += prev
		else:
			prev += 1	
	
	if(goal < K):
		print "Case #%d: %s" %(i+1, "IMPOSSIBLE")
		return
	print "Case #%d: %s" %(i+1, n_swaps)
	

n_cases = int(raw_input())
for i in xrange(n_cases):
	N, K, B, T =  map(int, stdin.readline().split())
	X = map(int, stdin.readline().split())
	V = map(int, stdin.readline().split())
	solve(i, X, V, K, B, T)