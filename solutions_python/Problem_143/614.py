#! /usr/bin/python

import sys
import math

def exec_test(A,B,K):

	print A
	print B
	print K

	res=0

	for a in xrange(A):
		for b in xrange(B):
			if( a&b < K):
				res=res+1

	return " %i" % res

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	num = fd.readline().split()
	num = map(lambda x: int(x), num)
	ret = exec_test(num[0], num[1], num[2])
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

