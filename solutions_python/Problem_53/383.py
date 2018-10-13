import sys
 
def f(N, K):
	if (K+1)%(2**N) == 0:
		return "ON"
	else:
		return "OFF"
 
inf = open(sys.argv[1])
T = int(inf.readline())
for i in range(T):
	N, K = [int(x) for x in inf.readline().split()]
	result = f(N, K)
	print "Case #%d: %s" % (i+1, result)