import codejam

lines = codejam.input("C")
while len(lines) > 0:
	[N, Q] = list(map(int, lines.pop(0).split(" ")))
	cities = []
	distance = {}
	for i in range(N):
		[E, S] = list(map(int, lines.pop(0).split(" ")))
		cities.append([E, S])
	for i in range(N):
		D = list(map(int, lines.pop(0).split(" ")))
		distance[i] = {}
		for j in range(len(D)):
			if D[j] != -1:
				distance[i][j] = D[j]
	answers = []
	for i in range(Q):
		[start, end] = list(map(lambda x: int(x) - 1, lines.pop(0).split(" ")))
		nodes = set()
		dists = {}
		for city in range(N):
			dist = {}
			for other in range(N):
				dist[other] = float("inf")
				nodes.add(other)
			dist[city] = 0
			while len(nodes) > 0:
				m = min(nodes, key = lambda x: dist[x])
				nodes.remove(m)
				for n in distance[m].keys():
					alt = dist[m] + distance[m][n]
					dist[n] = min(dist[n], alt)
			dists[city] = dist
		queue = [start]
		done = set()
		times = [float("inf")] * N
		times[start] = 0
		while len(queue) > 0:
			v = queue.pop(0)
			[energy, speed] = cities[v]
			for (city, d) in dists[v].items():
				if energy >= d and times[v] + d / speed < times[city]:
					times[city] = times[v] + d / speed
					if city in queue:
						queue.remove(city)
					queue.append(city)
		answers.append(str(times[end]))
	codejam.case(" ".join(answers))

codejam.finish()