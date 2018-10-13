import sys
import math

n = int(sys.stdin.readline())

def pal(s):
	s = str(s)
	return s == s[::-1]

def f(n):
	if not pal(n): return False
	m = int(math.sqrt(n) + 1e-100)
	if m*m != n: return False
	if not pal(m): return False
	return True

for t in xrange(n):
	A, B = map(int, sys.stdin.readline().split())
	ans = 0
	for i in xrange(A, B+1):
		if f(i):
			ans += 1
	print 'Case #%d:' % (t+1), ans


