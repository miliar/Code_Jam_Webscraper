import sys

sys.setrecursionlimit(5000)

def ns(S, Q, queries, switches, e, i):
	if i == Q:
		return 0
	if switches[e][i]:
		return switches[e][i]
	result = Q
	for ep in xrange(S):
		if ep != e:
			k = 0
			for j in xrange(i, Q):
				if queries[j] != ep:
					k += 1
				else:
					break
			result = min(result, ns(S, Q, queries, switches, ep, i + k) + 1)
	switches[e][i] = result
	return result

f = open(sys.argv[1])

N = int(f.readline())

for i in xrange(N):
	engines = {}
	queries = []
	S = int(f.readline())
	for j in xrange(S):
		e = f.readline().strip()
		engines[e] = j
	Q = int(f.readline())
	for j in xrange(Q):
		q = f.readline().strip()
		queries.append(engines[q])
	switches = [[None for q in xrange(Q)] for e in xrange(S)]
	result = min([ns(S, Q, queries, switches, e, 0) for e in xrange(S)]) - 1
	if Q == 0:
		result = 0
	print "Case #%d: %d" % (i + 1, result)
