from fractions import gcd

for test in xrange(int(raw_input())):
	times = sorted(int(x) for x in raw_input().split(' ')[1:])
	diffs = map(lambda i: times[i + 1] - times[i], range(len(times) - 1))
	T = reduce(gcd, diffs)
	print "Case #%d: %d" % (test + 1, (T - times[0] % T) % T)

