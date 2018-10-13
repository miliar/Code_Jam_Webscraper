import math 
t=int(input())

for i in xrange(1,t+1) :
	r,c,w=map(int,raw_input().split())
	slots=math.ceil(float(c)/w)
	print "Case #%d: %d"%(i,r*slots+w-1)
