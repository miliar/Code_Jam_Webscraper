# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np
from util import replace

T = int(raw_input())
for i in xrange(1, T + 1):
	D, N = [int(_) for _ in raw_input().split(" ")]
	K = np.zeros(N)
	S = np.zeros(N)
	for n in range(N):
		k, s = [int(_) for _ in raw_input().split(" ")]
		K[n] = k
		S[n] = s

	t = np.zeros(N)
	for n in range(N):
		t[n] = (D - K[n])/S[n]
		
#	print(D/np.max(t))
#	if np.sum(pan) == len(pan):
#		print "Case #{}: {}".format(i, num_flips)
#	else:
	print "Case #{}: {}".format(i, D/np.max(t))