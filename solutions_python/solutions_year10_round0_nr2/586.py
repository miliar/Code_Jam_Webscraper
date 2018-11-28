from fractions import *
In = open('file.in')
T = int(In.readline().split()[0])
for cnt in xrange(T):
	a = [int(i) for i in In.readline().split()]
	n = a[0]
	a[:1] = []
	a.sort()
	d = a[1] - a[0]
	p = 0
	for i in xrange(2,n):
		d = gcd(d,a[i] - a[i-1])
	y = d - a[0]%d
	for i in a:
		p = i % d
		if p == 0:
			y = 0
			break
		y = min(y,d - p)

	print 'Case #%d: %d' % (cnt+1,y)