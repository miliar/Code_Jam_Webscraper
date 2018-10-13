from __future__ import division
import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

for kkk in range(T):
	X,S,R,t,N = readlist()
	
	seg = []
	for i in range(N):
		b,e,w = readlist()
		seg.append((e-b, w + S))
		X -= e-b;
	seg.append((X, S));
	seg.sort(key=lambda x: x[1])
	#~ print seg
	
	total_time = 0
	for dist,speed in seg:
		time = dist/speed
		speedrun = (R + speed - S)
		# primii t pasi ii alerg
		trun = min(dist / speedrun, t)
		#~ print t,dist,speed,time,trun
		t -= trun
		dist -= trun * speedrun
		total_time += trun
		# acu merg incet
		total_time += dist / speed
		#~ print total_time
	# v = d/t => t = d/v
	
	print "Case #%d: %.10g" % (kkk+1, total_time)
