import sys

for kase in xrange(int(sys.stdin.readline())):
	R, k, N = [long(x) for x in sys.stdin.readline().split()]
	g = [long(x) for x in sys.stdin.readline().split()]

	if k >= sum(g):
		print 'Case #%d: %d' % (kase+1, R * sum(g))
		continue

	me = [-1] * N
	mr = [-1] * N
	cnt = 0
	pos = 0
	ride = 0
	while me[pos] == -1 and R > 0:
		me[pos] = cnt
		mr[pos] = ride
		free = k
		while free >= g[pos]:
			free -= g[pos]
			cnt += g[pos]
			pos = (pos + 1) % N
		ride += 1
		R -= 1
	
	step = ride - mr[pos]
	times = R / step
	cnt += times * (cnt - me[pos])
	R -= times * step

	while R > 0:
		free = k
		while free >= g[pos]:
			free -= g[pos]
			cnt += g[pos]
			pos = (pos + 1) % N
		R -= 1

	print 'Case #%d: %d' % (kase+1, cnt)
