for t in xrange(int(raw_input())):
	n = int(raw_input())

	for i in xrange(n, -1, -1):
		j = str(i)
		if all(j[x] <= j[x+1] for x in xrange(len(j)-1)):
			print "Case #%d: %d" % (t+1, i)
			break
