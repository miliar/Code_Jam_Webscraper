T = int(input())

for t in range(T):
	N, K = map(int, str(input()).split(' '))

	row = [False for _ in range(N)]

	y = 0
	z = 0

	for k in range(K):
		tab = []
		for S in range(N):
			if row[S] == False:
				Ls = 0
				Rs = 0

				#On left
				for i in reversed(range(0,S)):
					if row[i] == False:
						Ls += 1
					else:
						break

				#On right
				for i in range(S+1, N):
					if row[i] == False:
						Rs += 1
					else:
						break

				tab.append([S,Ls,Rs])

		tab.sort(key=lambda x: (-min(x[1],x[2]), -max(x[1],x[2]), x[0]) )
		row[tab[0][0]] = True
		if k == K-1:
			y = max(tab[0][1], tab[0][2])
			z = min(tab[0][1], tab[0][2])

	print("Case #{}: {} {}".format(t+1,y,z))