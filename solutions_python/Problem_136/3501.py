T = input()

for i in xrange(T):
	C, F, X = map(float, raw_input().split())
	cf, a = 2.0, 1
	T = X / cf
	while True:
		cf += F
		ct = X / cf
		for b in xrange(a):
			ct += C / (cf-(b+1)*F)
		if ct <= T:
			T = ct
			a += 1
		else:
			print "Case #%d: %.7f" % (i+1, T)
			break