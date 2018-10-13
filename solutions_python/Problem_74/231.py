#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	secs=0
	pos={'O':1,'B':1}
	idle={'O':0,'B':0}
	li=fin.readline().strip().split(" ")[1:]
	while li:
		r=li.pop(0)
		b=int(li.pop(0))
		t=max(abs(pos[r]-b)-idle[r],0)+1
		secs+=t
		pos[r]=b
		idle[r]=0
		idle[r=='B' and 'O' or 'B']+=t
	print "Case #%d: %d"%(case,secs)
