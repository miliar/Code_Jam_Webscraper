T = int(raw_input())

for t in xrange(1, T + 1):
	N = list(raw_input())

	result = list(N)
	
	cut = False
	for i in reversed(xrange(1, len(N))):
		if N[i] >= N[i - 1]:
			continue

		for j in xrange(i, len(N)):
			N[j] = '9'
		N[i - 1] = chr(ord(N[i - 1]) - 1)

	print 'Case #{}: {}'.format(t, int(''.join(N)))
