def snap(n,k):
	mask = 2**n
	return ((k%mask)+1) & mask
import sys
f = open(sys.argv[1], 'r')
cases = int(f.readline())
for case in xrange(cases):
	n,k = map(int,f.readline().split())
	if snap(n,k) > 0:
		onoff = 'ON'
	else:
		onoff = 'OFF'
		
	print 'Case #%d: %s' % (case+1,onoff)