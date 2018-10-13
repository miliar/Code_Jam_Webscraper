#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	N,L,H=map(int,fin.readline().split())
	notes=map(int,fin.readline().split())
	for i in xrange(L,H+2):
		if all([i%n==0 or n%i==0 for n in notes]): break
	print "Case #%d: %s"%(case,"NO" if i==H+1 else str(i))
