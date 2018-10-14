import sys, fractions

f = sys.stdin
C = int(f.readline())

for c in xrange(C):
	data = f.readline().split()
	N = int(data[0])
	events = [long(x) for x in data[1:]]
	events.sort()
	
	last = events[0]
	delta = []
	for n in xrange(N-1):
		delta.append(events[n+1]-events[n])
	
	gcd = delta[0]
	for d in delta:
		gcd = fractions.gcd(gcd, d)
		
	y = -last + (last/gcd)*gcd
	while y<0:
		y += gcd
	
	print "Case #%d: %d" %(c+1,y)