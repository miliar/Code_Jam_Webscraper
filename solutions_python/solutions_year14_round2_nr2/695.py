#!/usr/bin/env python

fo = open("B-small-attempt0 (1).in","r");
import sys
sys.stdout = open("output.out","w");
T = int(fo.readline())
for t in range(1, T + 1):
	
	a,b,k = map(lambda x: int(x), fo.readline().split(' '))
	count = 0
	#a = map(lambda x: str(x), fo.readline().split(' '))
	
	#a = map(lambda x: str(x), fo.readline().split(' '))
	
	for i in range(0,a):
		y = bin(i)
		#' '.join(format(ord(x), 'b') for m in y)
		#y = bin(str(i))
		for j in range(0,b):
			#z = bin(str(j))
			z = bin(j)
			#' '.join(format(ord(x), 'b') for m in z)
			x = i & j
			#print x
			if x < k:
				count+=1
		 
	 
	print 'Case #%d: %d' %(t,count)
