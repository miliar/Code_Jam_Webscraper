import os
from math import *

T = int(raw_input())

for case in range(0,T):
	D, N  = raw_input().split()
	time = []
	D = int(D)
	N = int(N)
	## Okay so I think all we need to do is determine the slowest horse
	## and then set the cruise speed to match that. 
	for horse in range(0,N):
		K, S = raw_input().split()
		time.append( (D - int(K)) / float(S))
	
	#~ print "times are" , time
	time.sort()
	slowest = time[-1]
	#~ print "slowest is " , slowest
	our_speed = D / slowest
	#~ print "the speed we are choosing is ", our_speed
	
	print "Case #" +str(case+1) + ": "  + str(our_speed)

 
 
