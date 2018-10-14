#! /usr/bin/env python
'''
Name: Sravan Bhamidipati
Date: 11th April, 2014
Purpose: 
'''

import sys
from decimal import *


with open(sys.argv[1]) as fd:
	for line_no, line in enumerate(fd):
		if line_no == 0:
			continue
		else:
			c, f, x = line.strip().split()
			c = Decimal(c)
			f = Decimal(f)
			x = Decimal(x)
			prev = x/2
			curr = (c/2) + (x/(2+f))
			n = 2

			while prev > curr:
				prev = curr
				two_nf = 2 + (n*f)
				curr = prev + ((c-x)/(two_nf-f)) + (x/two_nf)
				n += 1

			print 'Case #%d: %s' % (line_no, prev)
