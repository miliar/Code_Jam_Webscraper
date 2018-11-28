cas = int(raw_input())
for i in xrange(cas):
	C, F, X = map(float, raw_input().split(' '))
	ans , v = (0.0, 2.0)
	while X/v  > X/(v+F) + C/v:
		ans += C / v
		v += F
	ans += X / v
	print "Case #%d: %.8f" % (i + 1, ans)
