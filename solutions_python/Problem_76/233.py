#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	fin.readline()
	data=map(int,fin.readline().strip().split())
	if reduce(lambda x,y:x^y,data,0)==0: res=str(sum(data)-min(data))
	else: res="NO"
	print "Case #%d: %s"%(case,res)
