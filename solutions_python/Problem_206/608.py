def maxSpeed(D, K, S):
	T = 0
	for i in range(len(K)):
		t = (D - K[i]) / S[i]
		T = max(T, t)

	return '{0:.6f}'.format(D / T)

T = int(input())
for i in range(T):
	D, N = [int(p) for p in input().split()]
	K = []
	S = []
	for j in range(N):
		k, s = [int(p) for p in input().split()]
		K.append(k)
		S.append(s)
	print('Case #{}: {}'.format(i + 1, maxSpeed(D, K, S)))