for T in xrange(input()):
	r, t = [int(x) for x in raw_input().split()]
	s, count = (0, 0)
	while s <= t:
		s += 2 * r + 1
		r += 2
		count += 1
	print "Case #%d:"%(T+1), count - 1