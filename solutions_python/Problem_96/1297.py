import sys

T = int(sys.stdin.readline())
for i in xrange(T):
	line = sys.stdin.readline().strip()
	data = map(lambda s : int(s), line.split(' '))
	
	(S, p) = data[1:3]
	(c1, c2) = (p+2*max(p-1, 0), p+2*max(p-2, 0))

	n1 = sum(1 for j in data[3:] if j >= c1)
	n2 = sum(1 for j in data[3:] if c1 > j >= c2)
	print 'Case #%d: %d' % (i+1, n1+min(S,n2))
	