
def solve(A, B, K):
	c = A*B
	for a in xrange(K, A):
		for b in xrange(K, B):
			if a&b>=K:
				c -= 1
	return c

T = int(raw_input())
for t in xrange(1, T+1):
	A, B, K = map(int, raw_input().split())
	print "Case #{}: {}".format(t, solve(A,B,K))
