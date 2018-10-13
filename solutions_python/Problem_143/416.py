def f(A, B, K):
	r = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				r += 1
	return r

T = int(raw_input())
for i in range(T):
	A, B, K = map(int, raw_input().split())
	r = f(A, B, K)
	print 'Case #%d: %s' % (i + 1, r)
