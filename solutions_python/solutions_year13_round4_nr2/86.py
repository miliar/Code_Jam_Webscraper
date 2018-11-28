import itertools
import sys

def maxwins(n,k):
	w = dislog((1<<n)-k)-1
	return ((1<<w)-1)<<(n-w)
def minwins(n,k):
	w = n+1-dislog(k+1)
	return (1<<w)-1
def dislog(k):
	r = 0
	while k > 0:
		k >>= 1
		r += 1
	return r
# asserts f(a), ~f(b)
# search(n,f) = max k s.t.
# f(k)
def search(n,f):
	a, b = 0, 1<<n
	while a+1 != b:
		c = (a+b)//2
		if f(c):
			a = c
		else: b = c
	return a

T = int(sys.stdin.readline())
for t in xrange(T):
	n, p = map(int, sys.stdin.readline().split())
	alway = search(n, lambda k: (1<<n)-minwins(n,k) <= p)
	could = search(n, lambda k: (1<<n)-maxwins(n,k) <= p)
	print "Case #%d: %d %d" % (t+1, alway, could)

