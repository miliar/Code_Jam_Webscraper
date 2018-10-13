def solve(n, p, g):
	dist = [sum([1 for v in g if v%p == i]) for i in xrange(p)]
	if p == 2:
		return dist[0] + (1+dist[1]) / 2
	if p == 3:
		val = dist[0]
		take = min(dist[1], dist[2])
		val += take
		dist[1] -= take
		dist[2] -= take
		return val + (max(dist[1], dist[2]) + 2) / 3
	return 0



T = int(raw_input())
for case in xrange(1, T+1):
	n, p = map(int, raw_input().split())
	g = map(int, raw_input().split())
	solution = solve(n, p, g)
	print "Case #{}: {}".format(case, solution)


