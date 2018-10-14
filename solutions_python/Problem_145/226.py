#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import math
import sys

def gcd(a,b):
	while (b!=0):
		a = a % b
		tmp = a
		a = b
		b = tmp
	return a

if __name__ == "__main__":
	t = input()
	for caseIdx in xrange(1,t+1):
		p, q = map(int, raw_input().split('/'))
		g = gcd(p,q)
		p = p / g
		q = q / g

		# q must be 2^n
		tmp = q
		while ( tmp % 2 == 0 ):
			tmp = tmp / 2
		if tmp == 1:
			n = 1
			while ( p * 2 < q ):
				n = n + 1
				q = q / 2
			print "Case #%d: %d" % (caseIdx, n)
		else:
			print "Case #%d: impossible" % (caseIdx)
