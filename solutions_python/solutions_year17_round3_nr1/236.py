# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np

T = int(raw_input())
for i in xrange(1, T + 1):
	N, K = [int(_) for _ in raw_input().split(" ")]

	R = np.zeros(N)
	H = np.zeros(N)
	for n in range(N):
		R[n], H[n] = [int(_) for _ in raw_input().split(" ")]
	
	indices = np.argsort(R)
	R = R[indices]
	H = H[indices]
	R = R[::-1]
	H = H[::-1]
	C = R*H
#	print R, H
	out = np.zeros(N-K+1)
#	print(R,H,C)
	for n in range(N-K+1):
		indices = np.argsort(R[n+1:]*H[n+1:])
#		print(indices)
		tempC = C[n+1:][indices][::-1]
#		print(tempC)
		out[n] = np.pi*R[n]**2 +2*np.pi*R[n]*H[n] + np.sum(2*np.pi*tempC[:(K-1)])

#	print(out)
#	print(np.max(out))

	print "Case #{}: {:0.8f}".format(i, np.max(out))
		