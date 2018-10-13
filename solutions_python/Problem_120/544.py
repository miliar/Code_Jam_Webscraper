T = int(raw_input())
for _t in xrange(T):
	r, t = map(int, raw_input().split())
	a = 2
	b = 2*r-1
	c = -t
	r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
	print "Case #%d: %d" % (_t+1, int(r1))