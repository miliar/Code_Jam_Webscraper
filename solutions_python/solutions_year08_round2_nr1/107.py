#!/usr/bin/env python

from sys import exit, argv
f = open(argv[1])
n = int(f.readline())

for i in range(n):
	n,A,B,C,D,x0,y0,M = map(lambda i: int(i), f.readline().split(' '))
	X,Y=x0,y0
	points = []
	points.append((X,Y))
	triangles = []
	for j in range(1,n):
		X = (A*X+B) % M
		Y = (C*Y+D) % M
		points.append((X,Y))
	for a in points:
		for b in points:
			for c in points:
				if a == b or b == c or c == a: continue
				if (a[0] + b[0] + c[0]) % 3 == 0 and (a[1]+b[1]+c[1]) % 3 == 0:
					triangles.append(set([a,b,c]))
	print "Case #%d: %d" % (i+1,len(triangles)/6)
	

	
