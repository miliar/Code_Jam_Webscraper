#! /usr/bin/python

import sys
import math

def exec_test(P,Q):
	print P
	print Q

	P=(2**40)*P

	if P%Q!=0:
	 return " impossible"

	N=P/Q

	for n in xrange(40):
		if(N & (1<<(40-n))):
			res = n
			break

	return " %i" % res

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split('/')
	P=int(nums[0])
	Q=int(nums[1])
	ret = exec_test(P,Q)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

