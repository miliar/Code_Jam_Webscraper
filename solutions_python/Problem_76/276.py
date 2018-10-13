import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def xorsum(x):
	r = 0
	for a in x:
		r = r ^ a
	return r

def diff(a,b):
	a = list(tuple(a))
	b = list(tuple(b))
	for x in b:
		if x in a:
			a.remove(x)
	return a

for t in range(T):
	n = int(sys.stdin.readline())
	x = readlist()
	
	if xorsum(x) != 0:
		ans = "NO"
	else:
		x.sort()
		ans = sum(x[1:])
	print "Case #%d: %s" % (t+1, ans)
