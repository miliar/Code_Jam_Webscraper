import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for tc in xrange(1,T+1):
	N = int(f.readline())
	C = [int(c) - 1 for c in f.readline().split()]
	
	flags = [False] * len(C)
	cycles = []
	i = 0
	while i < len(C):
		cycle = []
		while not flags[i]:
			flags[i] = True
			cycle.append(i)
			i = C[i]
		cycles.append(cycle)
		while i < len(C) and flags[i]: i += 1
	res = sum( [len(c) for c in cycles if len(c) > 1] )
	print "Case #{0}: {1}".format(tc, res)
f.close()
