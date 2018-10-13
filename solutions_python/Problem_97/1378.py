import sys
sys.stdin = open('recycle.in')
sys.stdout = open('recycle.out', 'w')

n = input()
for i in xrange(n):
	sa, sb = raw_input().split(' ')
	a, b = int(sa), int(sb)
	count = 0
	for m in xrange(a, b+1):
		sn = sm = str(m)
		
		ns = set()
		for k in xrange(len(sm) - 1):
			sn = sn[-1] + sn[:-1]
			n = int(sn)
			if sn[0] != '0' and m < n <= b and n not in ns:
				count += 1
				ns.add(n)
	print "Case #%d: %d" % (i+1, count)