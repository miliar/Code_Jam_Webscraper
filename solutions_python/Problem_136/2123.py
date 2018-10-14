case = int(raw_input())

for t in xrange(1, case + 1):
	c, f, x = (float(i) for i in raw_input().split())

	tc = 0.0
	fc = 2.0
	res = x / fc
	while tc < res:
		tc += c / fc
		fc += f
		res = min(res, tc + x / fc)
	print 'Case #%d: %7f' % (t, res)