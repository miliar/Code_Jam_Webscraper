#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

T = int(sys.stdin.readline())

for cc in range(1, T+1):
	L, P, C = [int(s) for s in sys.stdin.readline().split()]
	num = 0
	t = L
	while t*C < P:
		num = num + 1
		t = t*C
	if num == 0:
		num = 0	
	else:
		num = int(math.log(num)/math.log(2)) + 1	
	print "Case #%d: %d"%(cc, num)	
	
