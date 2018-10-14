n = input()
for r in xrange(n):
	c, f, x = tuple(float(z) for z in raw_input().split(' '))
	k = 2.0
	t = 0
	while (c/k + x/(k+f)) < (x/k):
		t += c/k
		k += f
	print 'Case #%d: %.7f' % (r+1, t+x/k)
