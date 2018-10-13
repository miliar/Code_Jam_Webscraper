import sys

input = sys.stdin.readline().split()
N = int(input[0])
mem = dict()

def mincost(lo, hi, rel):
	# print "# mincost(", lo, ",", hi, ",", rel, ")"
	if not rel: return 0
	global mem
	if (lo, hi, rel) not in mem:
		answer = 9999999
		for r in rel:
			cand = hi - lo + mincost(lo, r - 1, frozenset(filter(lambda p: p < r, rel))) + mincost(r + 1, hi, frozenset(filter(lambda p: p > r, rel)))
			# print "# r", r, "cand", cand
			if cand < answer: answer = cand
		mem[(lo, hi, rel)] = answer
	return mem[(lo, hi, rel)]

for n in xrange(N):
	input = sys.stdin.readline().split()
	P = int(input[0])
	Q = int(input[1])
	input = sys.stdin.readline().split()
	release = set()
	for i in input: release.add(int(i))
	mem = dict()
	print 'Case #%d: %d' % (n + 1, mincost(1, P, frozenset(release)))

