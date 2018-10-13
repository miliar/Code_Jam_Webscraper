cont = 1
T = int(input())

while T:
	T -= 1

	[N, K] = [int(k) for k in input().split()]

	V = [N]
	L = []
	R = [N]

	for i in range(K - 1):
		for j in R:
			x = int((j - 1)/2)
			L.append(x)
			if j % 2 == 1:
				L.append(x)
			else:
				L.append(x + 1)

		L = sorted(L, reverse = True)
		
		R = L
		V.extend(L)
		L = []

		if len(V) > K + 1:
			break

	y = int((V[K - 1] - 1)/2)
	if V[K - 1] % 2 == 1:
		print("Case #", cont, ": ", y, " ", y, sep = '')
	else:
		print("Case #", cont, ": ", y + 1, " ", y, sep = '')
	cont += 1