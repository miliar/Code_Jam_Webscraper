for tt in xrange(1, int(raw_input()) + 1):
	r, t = map(int, raw_input().split())
	b, e = 0, (1 << 31)
	while b + 1 < e:
		m = (b + e) / 2
		s = (2 * r + 2 * m - 1) * m
		b, e = (m, e) if s <= t else (b, m)
	print "Case #%d: %d" % (tt, b)