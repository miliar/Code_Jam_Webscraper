import sys
import fractions
num_case = int(sys.stdin.readline())
caseno = 0
for line in sys.stdin.readlines():
	if caseno >= num_case:
		break
	caseno += 1
	sline = line.split()	
	llen = int(sline[0])
	vals = []
	for i in xrange(1, llen+1):
		vals.append(int(sline[i]))
	small = min(vals)
	for i in xrange(0, llen):
		vals[i] -= small
	g = 0		
	for i in xrange(0, llen):
		g = fractions.gcd(g, vals[i])
	#print g	
	extra = 0
	if small%g != 0:
		extra = 1
	k = small/g + extra
	print "Case #{0}: {1}".format(caseno, k*g - small)


