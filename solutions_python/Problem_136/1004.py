#!/usr/bin/python
import sys
arr=[]
i=0
first=True
for lines in sys.stdin:
	if first:
		T=int(lines)
		first=False
	else:
		i=i+1
		arr=lines.split()
		sum=0.0
		n=0.0
		C,F,X=float(arr[0]),float(arr[1]),float(arr[2])
		max1=X/2.0
		while True:
			n=n+1
			sum= sum+C/(2+(n-1)*F)
			min1=(X/(n*F+2) + sum)
			if min1 > max1:
				break
			else:
				max1=min1
		print "Case #%d: %f" %(i,max1)


