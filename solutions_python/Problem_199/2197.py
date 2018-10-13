# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np
from util import replace

N = int(raw_input())
for i in xrange(1, N + 1):
	S, K = [_ for _ in raw_input().split(" ")]
#	print(S,K)
	K = int(K)
	pan = list(S)
#	print(pan)
	replace(pan, '-', 0)
	replace(pan, '+', 1)
	pan = np.array(pan)
	num_flips = 0
	for k in range(len(S)-K+1):
		if pan[k] == 0:
			pan[k:k+K] = 1-pan[k:k+K]
#			print(pan)
			num_flips += 1
		
	if np.sum(pan) == len(pan):
		print "Case #{}: {}".format(i, num_flips)
	else:
		print "Case #{}: {}".format(i, 'IMPOSSIBLE')