t = input()
for i in xrange(1, t+1):
	output = 0.0
	c, f, x = map(float, raw_input().split())
	current = 2.0
	cookies = 0.0
	s = 0.0
	while True:
		# import pdb; pdb.set_trace()
		a = c/current
		s1 = a + x/(current + f)
		s2 = x/current

		if s1 > s2:
			s += s2
			break
		else:
			current += f
			s += a

	print "Case #%d: %.7f" % (i, round(s, 7))