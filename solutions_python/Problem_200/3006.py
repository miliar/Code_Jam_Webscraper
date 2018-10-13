for t in xrange(1, input() + 1):
	s = list(raw_input().strip())
	n = len(s)
	for i in xrange(n - 2, -1, -1):
		if s[i] > s[i + 1]:
			for j in xrange(i + 1, n):
				s[j] = '9'
			s[i] = str(int(s[i]) - 1)
	print "Case #" + str(t) + ": " + str(int(''.join(s)))