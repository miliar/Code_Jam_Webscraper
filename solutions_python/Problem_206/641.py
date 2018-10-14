from itertools import *		

inf = open("a.in", 'r')
outf = open("a2.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	horses = []
	d, n = map(int, inf.readline().split())
	for i in xrange(0, n):
		ki, si = map(int, inf.readline().split())
		horses.append((ki, si))
	horses.sort()
	#print horses
	
	k0, s0 = horses[0]
	ta = float(d - k0) / s0
	
	
	if (n > 1):
		for i in xrange(1, n):
			k, s = horses[i]		
			if (s0 > s):
				t = float(k - k0) / (s0 - s)
				m = k0 + s0 * t
				if (m < d):
					ta = max(ta, t + float(d - m) / s)
					
			
	v = float(d / ta)	
	
	outf.write("Case #" + str(tc + 1) + ": ")	
	outf.write( str("{0:.6f}".format(v)) + "\n")	
	
outf.close()
