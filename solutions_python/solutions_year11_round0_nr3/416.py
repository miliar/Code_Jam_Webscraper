#!/usr/bin/python
import sys
f = open(sys.argv[1])
cases = int(f.readline())
for case in range(1,cases+1):
	f.readline()
	l=map( int, f.readline().strip().split() )
	print "Case #%d:"%(case),
	if reduce(lambda x,y: x^y, l)==0:
		print reduce(lambda x,y: x+y, l)-min(l)
	else:
		print "NO"
