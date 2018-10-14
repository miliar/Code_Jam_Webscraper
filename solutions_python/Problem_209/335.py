from itertools import *		
from math import *	

inf = open("a.in", 'r')
outf = open("a.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):	
	n, k = map(int, inf.readline().split())
	r = []
	h = []
	rh = []
	for i in xrange(0, n):
		ri, hi = map(int, inf.readline().split())
		r.append(ri)
		h.append(hi)
		rh.append((ri * hi, ri, hi))
	rh.sort()
	rh.reverse()
	#print rh
	
	rm1 = 0
	hm1 = 0
	s1 = 0
	for i in xrange(0, k):
		s1 += 2 * rh[i][0]
		if (rh[i][1] > rm1) or ((rh[i][1] == rm1) and (rh[i][2] > hm1)):
			rm1 = rh[i][1]
			hm1 = rh[i][2]
	s1 += rm1 * rm1
	
	
	
	rh.sort(key=lambda x: x[1])
	rh.reverse()
	#print rh
	b = 0
	while (b < n) and (rh[b][1] == rh[0][1]):
		b += 1
	tmp = rh[b : ]
	tmp.sort()
	tmp.reverse()
	rh2 = rh[0 : b] + tmp	
	#print rh2
	
	rm2 = rh2[0][1]
	s2 = 0
	for i in xrange(0, k):
		s2 += 2 * rh2[i][0]
	s2 += rm2 * rm2	
	
	'''rm2 = 0
	hm2 = 0
	s2 = s1 - 2 * rm1 * hm1 - rm1 * rm1 
	for i in xrange(k + 1, n):
		if (rh[i][1] > rm2) or ((rh[i][1] == rm2) and (rh[i][2] > hm2)):
			rm2 = rh[i][1]
			hm2 = rh[i][2]
	for i in xrange(
	s2 += 2 * rm2 * hm2 + rm2 * rm2'''
	
	s = s1
	if (s2 > s) and (rm2 > rm1):
		s = s2 	 
	
	outf.write("Case #" + str(tc + 1) + ": ")	
	outf.write( str("{0:.9f}".format(s * pi)) + "\n")	
	
outf.close()
