#! /usr/bin/env pypy
T = input()
for i in xrange(1, T+1):
	N = input()
	d, l = zip(*(map(int, raw_input().split()) for j in xrange(N)))
	D = input()
	radius = [d[0]] + [0] * (N-1)
	for j in xrange(N):
		right = d[j] + radius[j]
		if right >= D:
			print 'Case #%d: YES' % i
			break
		for k in xrange(j+1, N):
			if right < d[k]:
				break
			radius[k] = max(radius[k], min(l[k], d[k] - d[j]))
	else:
		print 'Case #%d: NO' % i