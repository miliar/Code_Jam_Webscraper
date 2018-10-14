#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	fin.readline()
	li=map(int,fin.readline().strip().split())
	print "Case #%d: %.6f"%(case,len(filter(lambda (x,y):x+1!=y, enumerate(li))))
