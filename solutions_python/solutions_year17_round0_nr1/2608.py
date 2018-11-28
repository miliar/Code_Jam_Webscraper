for t in range(int(input())):
	S, K = input().split()
	S = [x == '+' for x in S]
	K = int(K)
	r = 0
	for i in range(len(S) - K + 1):
		if not S[i]:
			for j in range(i, i + K):
				S[j] ^= True
			r += 1
	if not all(S[1-K:]):
		r = 'IMPOSSIBLE'
	print("Case #{}: {}".format(t + 1, r))