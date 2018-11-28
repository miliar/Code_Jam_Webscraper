# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
N = int(fin.readline())
def gcd(x,y):
    while x:
        x, y = y % x, x
    return y

for case in range(1,N+1):
	code = map(int, fin.readline().split())
	n = code[0]
	t = code[1:]
	p = []
#	sub = [[0 for i in range (0,n)] for j in range(0,n)]
	for i in range(0,n):
		for j in range(0,i):
			if(i!=j):
				p.append(abs(t[i]-t[j]))
	g= p[0]
	p.sort()
	for i in range(1,len(p)):
		g= gcd(g,p[i])
		if(g == 1):
			break;
	#print g - t[0]%g
	if(g != 1 and t[0]%g != 0):
		print "Case #%d: %d" % (case,g - t[0]%g)
	else:
		print "Case #%d: %d" % (case,0)
	#print "Case #%d: OFF" % (case)
 
