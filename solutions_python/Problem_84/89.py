#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	h,w=map(int,fin.readline().split())
	art=[list(fin.readline().strip()) for l in range(h)]
	def inrange(i,j):
		return 0<=i and i<h and 0<=j and j<w
	possible=1
	for i in xrange(h):
		for j in xrange(w):
			if art[i][j]=='#':
				art[i][j]='/'
				if inrange(i,j+1) and art[i][j+1]=='#': art[i][j+1]='\\'
				else: possible=0
				if inrange(i+1,j) and art[i+1][j]=='#': art[i+1][j]='\\'
				else: possible=0
				if inrange(i+1,j+1) and art[i+1][j+1]=='#': art[i+1][j+1]='/'
				else: possible=0
		if not possible: break
	print "Case #%d:\n%s"%(case,"Impossible" if not possible else '\n'.join(map(lambda x:''.join(x),art)))
