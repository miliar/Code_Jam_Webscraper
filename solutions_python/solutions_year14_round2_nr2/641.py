T = input()
for t in xrange(T):
	A, B, K = [int(_) for _ in raw_input().split()]
	c = 0
	for i in xrange(A):
		for j in xrange(B):
			if i & j < K:
				c += 1
	print "Case #%d: %d" % (t+1,c)
