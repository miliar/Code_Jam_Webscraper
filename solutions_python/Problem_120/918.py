T = int(raw_input())
i = 1

while i <= T:
	s = raw_input().split()
	r, t = int(s[0]), int(s[1])
	n = int(((((2 * r - 1) ** 2) + 8 * t) ** 0.5 + 1 - 2 * r) / 4)
	while 2 * n * n - n + 2 * n * r > t:
		n -= 1
	print 'Case #%d: %d' % (i, n)
	i += 1
