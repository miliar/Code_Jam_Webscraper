T = int(raw_input().strip())
for t in range(1,T+1):
	D, N = map(int, raw_input().strip().split())
	K = [0]*N
	S = [0]*N
	for i in range(N):
		k, s = map(float, raw_input().strip().split())
		K[i] = k
		S[i] = s

	min_T = [0.0]*N
	for i in range(N):
		min_T[i] = (D - K[i])/S[i]
	t_max = max(min_T)
	ans = D/t_max

	print 'Case #{0}: {1:.6f}'.format(t, ans)

