import sys
from fractions import gcd

with open(sys.argv[1]) as f:
	C = int(f.readline())
	tc = 0
	for line in f:
		tc += 1
		#read a line of input
		t = [int(x) for x in line.split()[1:]]
		tmin = min(t)
		#calculate gcd of all t - tmin
		d = 0
		for ti in t:
			d = gcd(d, ti - tmin)
		#distance from tmin
		if tmin % d == 0:
			y = 0
		else:
			y = d * (tmin / d + 1) - tmin
		
		print "Case #{0}: {1}".format(tc, y)
