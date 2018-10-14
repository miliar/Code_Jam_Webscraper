for case in xrange(input()):
	s, k = raw_input().split()
	s = list(s)
	k = int(k)
	flips = 0

	for i in xrange(len(s) - k + 1):
		if s[i] == '-':
			flips += 1
			for j in xrange(i, i + k):
				s[j] = '+' if s[j] == '-' else '-'

	print 'Case #{}: {}'.format(case + 1, 'IMPOSSIBLE' if '-' in s else flips)
