for i in xrange(int(raw_input())):
	N, K = map(int, raw_input().split(" "))
	res = K & (2**(N) - 1) == 2**(N) - 1
	print "Case #%i: %s" % (i+1, "ON" if res else "OFF")
