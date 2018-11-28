def c(i, j):
	return i * j + 2 * (i + j)

def f(N, M, K):
	r = K
	for i in range(1, M - 1):
		for j in range(1, N - 1):
			if c(i, j) >= K:
				r = min(r, 2 * (i + j))
			if i < M - 2 and c(i + 1, j) >= K:
				r = min(r, 2 * (i + j) + (2 if K - c(i, j) >= j + 1 else 1))
			if j < N - 2 and c(i, j + 1) >= K:
				r = min(r, 2 * (i + j) + (2 if K - c(i, j) >= i + 1 else 1))
			if c(i, j) < K:
				r = min(r, 2 * (i + j) + K - c(i, j))
	return r

T = int(raw_input())
for i in range(T):
	N, M, K = map(int, raw_input().split())
	r = f(N, M, K)
	print 'Case #%d: %s' % (i + 1, r)
