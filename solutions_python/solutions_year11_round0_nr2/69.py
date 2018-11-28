import sys
import psyco
from collections import defaultdict
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readarray(foo): return [foo(x) for x in raw_input().split()]

def run_test():
	a = readarray(str)
	c = int(a[0])
	o = int(a[c + 1])
	s = a[c + o + 3]
	to = {}
	bad = defaultdict(set)
	for i in xrange(c):
		(x, y, z) = a[i + 1]
		to[tuple(sorted((x, y)))] = z
	for i in xrange(o):
		(x, y) = a[c + i + 2]
		bad[x].add(y)
		bad[y].add(x)
	res = []
	for ch in s:
		if res:
			prev = res[-1]
			t = tuple(sorted((prev, ch)))
			if t in to:
				res[-1] = to[t]
				continue
		for x in bad[ch]:
			if x in res:
				res = []
				break
		else:
			res.append(ch)
	return str(res).replace("'", '')

for test in range(int(raw_input())):
	dbg("Test %d\n" % (test + 1))
	print "Case #%d: %s" % (test + 1, run_test())
