import sys

li = iter(sys.stdin)
t = int(next(li).strip())

for i in xrange(t):
	ch1 = int(next(li).strip())
	grid1 = [map(int, next(li).split()) for j in xrange(4)]
	ch2 = int(next(li).strip())
	grid2 = [map(int, next(li).split()) for j in xrange(4)]

	r = set(grid1[ch1-1]) & set(grid2[ch2-1])
	if len(r) == 0:
		print 'Case #%d: Volunteer cheated!' % (i+1)
	elif len(r) == 1:
		print 'Case #%d: %d' % (i+1, next(iter(r)))
	else:
		print 'Case #%d: Bad magician!' % (i + 1)
