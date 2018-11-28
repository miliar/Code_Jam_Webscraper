cases = int(raw_input())
for case in xrange(1, cases + 1):
	a, b = map(int, raw_input().split())
	digits, pairs = len(str(a)), 0
	mask = 10 ** digits
	for n in xrange(a, b + 1):
		joined = n * (mask + 1)
		rotated = set()
		for d in xrange(digits-1):
			joined /= 10
			rotated.add(joined % mask)
		for m in rotated:
			if n < m <= b:
				pairs += 1
	print 'Case #%d: %d' % (case, pairs)