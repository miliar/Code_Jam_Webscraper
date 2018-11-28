import os
import array
from itertools import *
f = open("A-small-attempt0.in",'r');
g = open("results1.dat",'w')
n = int(f.readline())

for l in range(n):
	p = map(int, (f.readline()).split())
	n = p[0]
	pd = p[1]
	pg = p[2]
	
	if ((pg == 100 and pd != 100) or (pg == 0 and pd != 0)):
		possible = False
	else:
		possible = False
		for d in range(1,n+1):
			wd = pd / 100.0 * d
#			print wd
			if (wd == int(wd)):
				possible = True
#	print possible
	
	if possible:
		g.write("Case #" + repr(l+1) + ": Possible\n")
	else:
		g.write("Case #" + repr(l+1) + ": Broken\n")
	
f.close()
g.close()

#print sum(i*j for (i,j) in zip(l1,l2))





