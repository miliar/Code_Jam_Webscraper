#!/usr/bin/python

t=int(raw_input())

def barvy(k, r):
	return 2*k*r+((4*k-2)*k)/2

def find(r, t):
	le=1
	ri=800000000
	while le<ri:
		s=(le+ri+1)/2
		if barvy(s, r)<=t:
			le=s
		else:
			ri=s-1
	return le

for i in range(0, t):
	ra=raw_input()
	s=ra.partition(' ')
	r=int(s[0])
	t=int(s[2])
	print "Case #"+str(i+1)+": "+str(find(r, t))

