import sys

def gcd(a,b):
	while b!=0:
		(a,b) = (b, a % b)
	return a
	

C=int(sys.stdin.readline())
for case in range(C):
	t = map(int, sys.stdin.readline().split())[1:]
	N = len(t)
	dt = [abs(t[i] - t[i-1]) for i in range(N)]
#	print dt
	T = reduce(gcd, dt)
#	print T
	cy = [(T - x % T) % T for x in t]
	y = min(cy)
	print "Case #%d: %s" % (case+1, y)
