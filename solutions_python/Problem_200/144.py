import math

T = int(raw_input().strip())
for t in xrange(1,T+1):
	n = int(raw_input().strip())
	p10 = 1
	while p10*10 <= n:
		p10 *= 10
	
	changed = 1
	while changed:
		changed = 0
		p = p10
		while 10 <= p:
			d1 = n/p%10
			d2 = n/(p/10)%10
			if d2 < d1:
				n = (n - p)/p*p + p-1
				changed = 1
			p /= 10
			
	print "Case #%d: %d"%(t,n)
