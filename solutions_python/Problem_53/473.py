numInputs = int(raw_input())
for iter in xrange(numInputs):
	N, K = [long(val) for val in raw_input().strip().split()]
	if (K + 1) % (1 << N) == 0:
		print "Case #%i: ON" % (iter + 1)
	else:
		print "Case #%i: OFF" % (iter + 1)
