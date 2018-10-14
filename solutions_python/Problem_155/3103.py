debug = False
T = int(raw_input())
for k in xrange(T):
	line = raw_input()
	smax, s = line.split()
	smax = int(smax)
	r = 0
	c = 0

	for i in xrange(smax+1):
		diff = 0
		if c < i:
			diff = i - c
			r += diff
		c += int(s[i]) + diff
		if debug:
			print "\tDEBUG(", k, "):","r=", r, "c=", c, "i=", i

	print "Case #" + str(k+1) + ": " + str(r)
