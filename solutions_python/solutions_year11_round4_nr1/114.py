from sys import stdin
import math
import bisect
import itertools

for c in xrange(1, 1+int(stdin.readline().strip())):
	x,s,r,t,n = [int(z) for z in stdin.readline().split()]
	ww = []
	td = 0
	for z in xrange(n):
		st, end, spd = [int(z) for z in stdin.readline().split()]
		dist = end-st
		ww.append( (spd, dist) )
		td+=dist
	ww.append( (0,x-td) )
	ww.sort()
	totaltime = 0
	while len(ww)>0:
		maxrd = (ww[0][0]+r)*t
		if maxrd > ww[0][1]: #> walkway - run whole way
			timerunning = float(ww[0][1])/(ww[0][0]+r)
			t -= timerunning
			totaltime += timerunning
			ww.pop(0)
		else: # less than walkway - run for a bit, walk for a bit
			walkdist = ww[0][1]- maxrd
			walktime = float(walkdist) / (ww[0][0]+s)
			totaltime += t + walktime
			ww.pop(0)
			t = 0
		#print ww
	print "Case #{0}: {1}".format(c, totaltime)
			
		