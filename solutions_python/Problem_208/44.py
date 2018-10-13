Cases = int(input())
Colors = "ROYGBV"

for Case in range(Cases):
	N,Q = map(int,input().split())
	H = [tuple( map(int,input().split()) ) for _ in range(N)]
	G = [ list(map(int,input().split())) for _ in range(N) ]
	q = [tuple( map(int,input().split()) ) for _ in range(Q)]
	#print(H)
	#print(G)
	#print(q)

	W = [[1e30]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if G[i][j] != -1:
				W[i][j] = G[i][j]
	for k in range(N):
		for i in range(N):
			for j in range(N):
				W[i][j] = min(W[i][j], W[i][k]+W[k][j])

	T = [[1e30]*N for _ in range(N)]

	for u in range(N):
		for v in range(N):
			if W[u][v] <= H[u][0]:
				T[u][v] = min(T[u][v], W[u][v] / H[u][1])

	w = [[1e30]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			w[i][j] = T[i][j]
	for k in range(N):
		for i in range(N):
			for j in range(N):
				w[i][j] = min(w[i][j], w[i][k]+w[k][j])

	ans = ' '.join(["%.10f" % w[a-1][b-1] for a,b in q])
	print('Case #%d: %s' % (Case+1, ans))