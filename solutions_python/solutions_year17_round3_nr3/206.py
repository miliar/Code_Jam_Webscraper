# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np

T = int(raw_input())
for i in xrange(1, T + 1):
	N, K = [int(_) for _ in raw_input().split(" ")]
	U = float(raw_input())
	P = [float(_) for _ in raw_input().split(" ")]

	P = np.sort(P)	
	
	for n in range(N-1):
		dp = P[n+1]-P[n]
		if U >= dp*(n+1):
			U = U - dp*(n+1)
			P[:n+1] = P[n+1]
		else:
			P[:n+1] = P[:n+1] + U/(n+1)
			U = 0
			break
		
	P = P + U / N
	
	print "Case #{}: {:0.8f}".format(i, np.prod(P))
		