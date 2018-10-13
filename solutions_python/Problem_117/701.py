import sys
T = int(sys.stdin.readline())

for t in range(T):
	N, M = map(int, sys.stdin.readline().strip().split())
	G = [None]*N
	for n in range(N):
		G[n] = [h for h in map(int, sys.stdin.readline().strip().split())]
	V = [[100]*M for n in range(N)]

	for n in range(N):
		for m in range(M):
			if G[n][m] == max(G[n]):
				for i in range(M):
					if V[n][i]>G[n][m]:
						V[n][i]=G[n][m]
			if G[n][m] == max([G[i][m] for i in range(N)]):
				for i in range(N):
					if V[i][m]>G[n][m]:
						V[i][m]=G[n][m]

	found = False
	for n in range(N):
		for m in range(M):
			if V[n][m]!=G[n][m]:
				found=True
				print("Case #%s: NO" % (str(t+1)))
				break
		if found: break
	if not found:
		print("Case #%s: YES" % (str(t+1)))
