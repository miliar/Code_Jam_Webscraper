def solve(N, Q, horses, routes, pairs):
	sol = []
	graph = [[] for _ in xrange(N)]
	for i in xrange(N):
		for j in xrange(N):
			if routes[i][j] != -1:
				graph[i].append((j, routes[i][j]))
	dists = [[1e20 for i in xrange(N)] for j in xrange(N)]
	for city in xrange(N):
		dists[city][city] = 0
		for dest, dist in graph[city]:
			dists[city][dest] = dist
	# Floyd-Warshall on distances
	for k in xrange(N):
		for i in xrange(N):
			for j in xrange(N):
				if dists[i][j] > dists[i][k] + dists[k][j]:
					dists[i][j] = dists[i][k] + dists[k][j]
	# time to reach by horse from horse's hometown
	h_times = [[1e20 for i in xrange(N)] for j in xrange(N)]
	for h in xrange(N):
		mx_d, sp = horses[h]
		for j in xrange(N):
			if dists[h][j] <= mx_d:
				h_times[h][j] = dists[h][j] / float(sp)
	# Floyd-Warshall on time to reach by horse
	for k in xrange(N):
		for i in xrange(N):
			for j in xrange(N):
				if h_times[i][j] > h_times[i][k] + h_times[k][j]:
					h_times[i][j] = h_times[i][k] + h_times[k][j]
	for u, v in pairs:
		sol.append(h_times[u-1][v-1])
	return ' '.join(map(str, sol))


T = int(raw_input())
for case in xrange(1, T+1):
	N, Q = map(int, raw_input().split())
	horses = [map(int, raw_input().split()) for _ in xrange(N)]
	routes = [map(int, raw_input().split()) for _ in xrange(N)]
	pairs = [map(int, raw_input().split()) for _ in xrange(Q)]

	solution = solve(N, Q, horses, routes, pairs)
	print "Case #{}: {}".format(case, solution)


