import sys

def preCompute(g, k):
	'''For each position in g computes the money earned and the next position'''
	if sum(g) < k: #all groups fit in the coaster
		return [[sum(g),0]] * len(g)
	
	tbl = []
	N = len(g)
	for i in xrange(N):
		s = 0
		j = i
		while s + g[j] <= k:
			s += g[j]
			j = (j + 1) % N
		tbl.append([s, j])
	return tbl

with open(sys.argv[1]) as f:
	T = int(f.readline())
	for tc in xrange(1, T + 1):
		R, k, N = [int(x) for x in f.readline().split()]
		g = [int(x) for x in f.readline().split()]
		tbl = preCompute(g, k)
		
		s = 0
		pos = 0
		for i in xrange(R):
			s += tbl[pos][0]
			pos = tbl[pos][1]
		print "Case #{0}: {1}".format(tc, s)
