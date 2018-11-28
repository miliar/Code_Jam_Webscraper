T = int(raw_input())

for t in xrange(1, T + 1):
	S, K = raw_input().split()
	S = list(S)
	K = int(K)

	result = 0

	for i, p in enumerate(S):
		if p == '+':
			continue

		if i + K > len(S):
			result = 'IMPOSSIBLE'
			break

		for j in xrange(K):
			S[i + j] = '+' if S[i + j] == '-' else '-'

		result += 1		

	print 'Case #{}: {}'.format(t, result)
