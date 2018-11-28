t = int(raw_input());

for cs in xrange(t):
	c, f, x = map(float, raw_input().split())
	t, r = 0.0, 2.0
	while x/(r+f) + c/r <= x/r:
		t += c/r
		r += f
	t += x/r

	print "Case #%d: %.8f" % (cs+1, t)
	
