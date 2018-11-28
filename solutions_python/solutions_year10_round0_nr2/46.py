import fractions

tests = int(raw_input())
for test in range(1, tests + 1):
	line = raw_input().split()
	n = int(line[0])
	t = map(int, line[1:])
	t.sort()
	g = t[1] - t[0]
	for i in range(2, n):
		g = fractions.gcd(g, t[i] - t[i-1])
	if t[0] % g == 0:
		print 'Case #%d: 0' % (test)
	else:
		print 'Case #%d: %d' % (test, g - (t[0] % g))