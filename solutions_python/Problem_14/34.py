#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import math
def gcd(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a


def area(bx,by,cx,cy):
	return abs((bx*cy) - (by*cx))

def process(f):
	line = f.readline()
	[n,m,a] = [ int(x) for x in line.split(' ') ]
	if a==0:
		return "0 0 0 0 0 0"
	
	for bx in range(0, n+1):
		for cy in range(0, m+1):
			if bx*cy == a:
				by = 0
				cx = 0
				if a==area(bx,by,cx,cy):
					return "0 0 %(bx)d %(by)d %(cx)d %(cy)d" %locals()

			for cx in range(1, n+1):
				by = (bx*cy-a) / cx
				if by>0 and by<=m:
					if a==area(bx,by,cx,cy):
						return "0 0 %(bx)d %(by)d %(cx)d %(cy)d" %locals()

				by = (bx*cy+a) / cx
				if by>0 and by<=m:
					if a==area(bx,by,cx,cy):
						return "0 0 %(bx)d %(by)d %(cx)d %(cy)d" %locals()
	
	return "IMPOSSIBLE"
	
def main():
	f = sys.stdin
	cases = int(f.readline())
	for case in range(1, cases+1):
		result = process(f)
		print "Case #%(case)d: %(result)s" % locals()
	f.close()
			 
if __name__ == '__main__':
	sys.exit(main())


