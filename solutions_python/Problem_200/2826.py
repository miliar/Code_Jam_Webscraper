T = int(raw_input())
for tc in range(1, T+1):
	a = map(int, raw_input().strip())
	n = len(a)
	mv = 9
	for i in reversed(range(0, n)):
		if a[i] <= mv:
			mv = a[i]
		else:
			a[i] = mv = a[i] -1
			for j in range(i + 1, n):
				a[j] = 9
	print 'Case #{0}: {1}'.format(tc, long(''.join(map(str, a))))
