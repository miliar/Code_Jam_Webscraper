import math

T = int(input())

for i in range(T):
	N, K = [int(i) for i in input().split()]

	pankakes = []

	maxR = 0

	for j in range(N):
		ri, hi = [int(i) for i in input().split()]
		if ri > maxR:
			maxR = ri
		pankakes.append((ri, hi))

	pankakes.sort(key=lambda p:p[0], reverse=True)

	best_result = 0


	for p in range(1+N-K):
		result = math.pi*(pankakes[p][0]**2) + 2 * math.pi * pankakes[p][0] * pankakes[p][1]
		copy = list(pankakes)
		copy = copy[p+1:]
		copy.sort(key=lambda p: p[0]*p[1], reverse=True)

		for o in range(K-1):
			result += 2 * math.pi * copy[o][0] * copy[o][1]
			
		if result > best_result:
			best_result = result

	print("Case #{}: ".format(i+1)+str(best_result))