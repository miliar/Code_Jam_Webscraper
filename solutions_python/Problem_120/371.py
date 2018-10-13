import sys
import math

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	ar = sys.stdin.readline().split()
	R = int(ar[0])
	L = int(ar[1])
	lo, hi = 0, 10**9
	while math.floor(hi) != math.floor(lo):
		m = (hi+lo) / 2.0
		t = (2*R+1+2*m)*(m+1)
		if t > L:
			hi = m
		else:
			lo = m
#k = (-(2*R+3) + math.sqrt((2*R+3)**2-8*(2*R+1-L))) / 4.0
	print "Case #%d: %d" % (T, math.floor(lo)+1)

