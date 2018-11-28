def floyd_warshall(d):
	n = len(d)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if d[i][k] == -1 or d[k][j] == -1:
					continue
				if d[i][j] > d[i][k] + d[k][j] or d[i][j] == -1:
					d[i][j] = d[i][k] + d[k][j]
	return d

getline = lambda: [int(x) for x in raw_input().split()]
INF = 10**12

T = int(raw_input())
for test_case in range(T):
	N,Q = getline()
	horses = [getline() for _ in range(N)]
	d = [getline() for _ in range(N)]
	mail = [getline() for _ in range(Q)]
	d = floyd_warshall(d)

	answers = []
	for [u,v] in mail:
		u,v = u-1, v-1
		dp = [INF for _ in range(N)]
		dp[u] = 0
		visited = set()
		neighbours = [u]
		while neighbours:
			neighbours = [x for x in neighbours if x not in visited]
			i = sorted(neighbours, key=lambda x: dp[x])[0]
			visited.add(i)
			if i == v:
				answers.append(dp[v]) 
				break
			[e,s] = horses[i]
			for j in range(N):
				if j in visited: continue
				if d[i][j] == -1 or e < d[i][j]:
					continue
				t = float(d[i][j])/s
				dp[j] = min(dp[j], dp[i] + t)
				neighbours.append(j)
	
	print "Case #%s: %s"%(test_case+1, " ".join(["%.10f"%x for x in answers]))
