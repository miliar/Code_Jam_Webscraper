T = int(input())

for i in range(1, T+1):
	N = input()
	N = list(map(int, list(str(N))))
	for c in range(len(N)-1, 0, -1):
		if N[c] < N[c-1]:
			for j in range(len(N)-1, c-1, -1):
				N[j] = 9
			N[c-1] = N[c-1] - 1
	result = int("".join(map(str, N)))
	print(f"Case #{i}: {result}")
