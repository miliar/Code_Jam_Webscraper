t = int(raw_input());

for cs in xrange(t):
	n, a, b = int(raw_input()), sorted(map(float, raw_input().split())), sorted(map(float, raw_input().split()))
	
	i, p = 0, n
	for j in xrange(n):
		if b[j] > a[i]:
			p -= 1
			i += 1
	
	a, b = b, a
	i, q = 0, 0
	for j in xrange(n):
		if b[j] > a[i]:
			q += 1
			i += 1
	
	print "Case #%d: %d %d" % (cs+1, q, p)
	
