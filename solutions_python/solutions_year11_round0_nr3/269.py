import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for tc in xrange(1,T+1):
	N = int(f.readline())
	C = [int(c) for c in f.readline().split()]
	res = "NO"
	if reduce(lambda x,y: x^y, C) == 0:
		res = sum(C) - min(C)
	print "Case #{0}: {1}".format(tc, res)
f.close()
