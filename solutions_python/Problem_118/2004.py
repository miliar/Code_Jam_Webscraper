#!/usr/bin/python
import sys
from math import sqrt

def is_pal(x):
	r=[]
	while x>0:
		r.append(x%10)
		x=x/10
	for x in range(len(r)/2):
		if r[x]!=r[len(r)-1-x]:
			return False
	return True

case=1
for line in sys.stdin:
	line=line.split()
	if len(line)>1:
		count=0
		#ok now use it
		a,b=map(int,line)
		sa,sb=map(int,map(sqrt,[a,b]))
		while sa*sa<a:
			sa+=1
		while sb*sb>b:
			sb-=1
		for x in range(sa,sb+1):
			if is_pal(x) and is_pal(x*x):
				count+=1
		print "Case #%d: %d" % (case,count)
		case+=1
