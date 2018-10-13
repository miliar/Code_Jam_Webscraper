for case in xrange(input()):
	n = map(int, list(raw_input()))

	for i in xrange(len(n) - 1):
		if any(n[j] < n[i] for j in xrange(i, len(n))):
			if n[i + 1] > n[i]:
				n[i + 1] -= 1
				for j in xrange(i + 2, len(n)):
					n[j] = 9
			else:
				n[i] -= 1
				for j in xrange(i + 1, len(n)):
					n[j] = 9
			break

	print 'Case #{}: {}'.format(case + 1, int(''.join(str(x) for x in n)))