dump = open('BL.in', 'r').readlines()

test_cases = int(dump[0][:-1])

for t in xrange(test_cases):
	print 'Case #{}:'.format(t+1),
	CF, F, G = map(float, dump[t+1][:-1].split(' '))
	V = 2.0
	for N in xrange(100000):
		if (1 / (V + N * F)) * (G - CF) < G / (V + (N + 1) * F):
			print CF * sum([1 / (V + n * F) for n in xrange(N)]) + G / (V + N * F)
			break
