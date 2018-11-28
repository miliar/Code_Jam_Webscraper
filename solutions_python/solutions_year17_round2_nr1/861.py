for cas in xrange(1,1+input()):
	print "Case #%s:" % cas,
	d,n = map(int,raw_input().split())
	t = 0
	for i in range(n):
		k,s = map(float,raw_input().split())
		t = max([t,(d-k)/s])

	print "{0:.6f}".format(d/t) 