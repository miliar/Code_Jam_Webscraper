def dfs(v, E, R, maxE):
	if len(v) == 1:
		return v[0]*E

	best = 0
	for e in xrange(E+1):
		best = max(best, dfs(v[1:], min(maxE, E-e+R), R, maxE) + v[0]*e)

	return best

T = int(raw_input())
for _t in xrange(T):
	E, R, N = map(int, raw_input().split())
	V = map(int, raw_input().split())
	print "Case #%d: %d" % (_t+1, dfs(V, E, R, E))