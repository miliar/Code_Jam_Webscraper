#!/usr/bin/python
t=int(input())
for i in xrange(t):
	string=raw_input()
	x,r,c = string.split()
	x=int(x)
	r=int(r)
	c=int(c)
	if (x/2 <= r and x <= c and c%x==0) or (x/2 <= c and x <= r and r%x==0) or (x<=c and x<=r):
		if (x==3 and (c == 1 or r == 1)) or ((x<=c and x<=r) and (x==2 and c*r%2!=0)) or( x==4 and (c<3 or r<3)) or (x==3 and c*r%3!=0):
			print "Case #%d: %s" %(i+1 ,"RICHARD")	
		else:			
			print "Case #%d: %s" %(i+1 ,"GABRIEL")
	else:
		print "Case #%d: %s" %(i+1 ,"RICHARD")
