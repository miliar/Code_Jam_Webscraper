import sys

def rc(N):
	x = "%d"%N
	for i in xrange(len(x) - 1):
		x = x[1:] + x[0]
		if x[0] != '0':
			yield int(x)

bound = 2000001
mrcs = [42] * bound
def mrc(N):
	if mrcs[N] == 42:
		mrcs[N] = set((N, x) for x in rc(N) if N < x)
	return mrcs[N]
	
def count(A, B):
	sum = 0
	for N in xrange(A, B+1):
		for p, q in mrc(N):
			if q <= B: sum += 1
	return sum
	
f = open(sys.argv[1], 'r')
i = -1
for l in f:
	i += 1
	if i == 0: continue
	A, B = [int(x) for x in l.split()]
	print "Case #%d: %d"%(i, count(A, B))