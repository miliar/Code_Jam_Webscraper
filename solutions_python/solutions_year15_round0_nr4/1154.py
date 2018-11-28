T = int(input())
for t in range(T):
	X, N, M = map(int, input().split())
	N, M = min(N, M), max(N, M)
	f = False
	S = N * M
	if X == 2 and not ((N > 1 or M > 1) and S % X == 0):
		f = True
	elif S % X != 0 or X >= (2 * N + 1) or (X >= (M + N - 2) and X > 3):
		f = True
	if X > N and X > M:
		f = True
	print('Case #', t + 1, ': ', 'RICHARD' if f else 'GABRIEL', sep='')