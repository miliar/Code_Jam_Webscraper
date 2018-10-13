import sys
import math

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	ar = map(int, sys.stdin.readline().split())
	N, X, Y = ar[0], ar[1], ar[2]
	X = abs(X)
	n = (X+Y)/2 + 1
	full = n + n*(n-1)*2
	emp = (n-1) + (n-1)*(n-2)*2
	if full <= N: ans = 1.0
	elif N <= emp: ans = 0.0
	elif X == 0: ans = 0.0
	else:
		d = N - emp
		side = 2*(n-1)
		if d-side >= Y+1: ans = 1.0
		else:
			win = 0
			choose = 1
			limit = d - (Y+1)
			for i in xrange(limit+1):
				if i > 0:
					choose = (choose*(d-i+1)) / i
				win += choose
			if win == 0: ans = 0.0
			else:
				ans = math.exp(math.log(win) - d*math.log(2))
				print >> sys.stderr, math.log(win), d*math.log(2)
	print "Case #%d: %.9f"%(T,ans)
