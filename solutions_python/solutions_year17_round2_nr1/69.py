for T in xrange(1, input() + 1):
	D, N = map(int, raw_input().split())
	t = 0
	for _ in xrange(N):
		k, s = map(int, raw_input().split())
		t = max(t, (D - k) / (s * 1.0))
	print "Case #%d: %.10f" % (T, D / t)