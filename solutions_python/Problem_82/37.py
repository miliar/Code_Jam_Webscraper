import sys
from sys import stdin

for t in xrange(1, 1+int(stdin.readline().strip())):
	ps=[]
	c, d = [int(z) for z in stdin.readline().split()]
	for pt in xrange(0,c):
		p,v = [int(z) for z in stdin.readline().split()]
		for q in xrange(0,v):
			ps.append(p)
	#print ps
	moves = [0]*len(ps)
	last=ps[0]
	mx = 0
	for i in xrange(1,len(ps)):
		dist = last+d-ps[i]
		#print ps[i], last, dist
		moves[i] = 0 if dist < 0 else dist
		last = ps[i] + moves[i]
		mx = moves[i] if moves[i] > mx else mx
	#print moves
	print "Case #{0}: {1}".format(t, float(mx)/2)
		
