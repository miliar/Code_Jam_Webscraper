#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
# Johan Musaeus Bruun, 20100523

# mate A.in A.sol
# ./A.py < A.in | tee A.out
# diff -w A.sol A.out

import sys
from numpy import *

def main(fin):
	T = int(fin.readline())
	# T = test case number
	
	for t in range(1,T+1):
		N = int(fin.readline())
		# N = number of lines in case t
		
		W = 2
		H = N
		# Read matrix from file
		lines = fromfile(fin, sep=' ', count=H*W, dtype=int16).reshape(H,W)
		
		res = 0
		for i in range(N):
			for j in range(i,N):
				Ai = lines[i,0]
				Bi = lines[i,1]
				Aj = lines[j,0]
				Bj = lines[j,1]
				if (Ai > Aj and Bi < Bj) or (Ai < Aj and Bi > Bj):
					res += 1		
		print "Case #%d: %s" % (t, res)
	exit()


################################################################

if __name__ == '__main__':
	try:
		#fin = open("A-test.in", 'r')
		fin = sys.stdin 
		main(fin)
	except IOError:
		print "File I/O error!"
