import sys

fi = iter(sys.stdin)

T = int(next(fi))
for t in xrange(T):
	tt = 0.0
	C, F, X = map(float, next(fi).split())
	rate_mult = 0

	while True:
		rate = 2.0 + F * rate_mult
		next_rate = 2.0 + F * (rate_mult + 1)
		t1 = X / rate
		t2 = (C / rate) + X / next_rate

		if t1 < t2:
			tt += t1
			break

		tt += C / rate
		rate_mult += 1

	print 'Case #%d: %.7f' % (t + 1, tt)
