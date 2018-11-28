#!/usr/bin/env python
# -*- coding: utf8 -*-
# Johan Musaeus Bruun, 20090903

# mate A.in A.sol
# ./A.py < A.in | tee A.out
# diff -w A.sol A.out

import sys

def main(fin):
	T = int(fin.readline())
	# T = test case number
	
	for t in range(1,T+1):
		N, K = map(int, fin.readline().split())
		res = process(N,K)
		print "Case #%d: %s" % (t, res)
	exit()


def process(N,K):
	e = 2 ** N
	k = K % e
	res = "OFF"
	if k == e-1:
		res = "ON"
	return res

################################################################

if __name__ == '__main__':
	try:
		#fin = open("A-test.in", 'r')
		fin = sys.stdin 
		main(fin)
	except IOError:
		print "File I/O error!"
