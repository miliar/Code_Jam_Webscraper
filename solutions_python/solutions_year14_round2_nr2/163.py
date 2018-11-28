import sys

def solve(a, b, k):
	s = 0
	for i in xrange(a):
		for j in xrange(b):
			if (i & j) < k:
				s += 1
	return s

T = int(sys.stdin.readline())
for t in range(1, T + 1):
	(a, b, k) = [int(x) for x in sys.stdin.readline().split()]
	print "Case #" + str(t) + ":", solve(a, b, k)