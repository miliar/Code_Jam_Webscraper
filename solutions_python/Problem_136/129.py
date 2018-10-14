#! /usr/bin/python

import sys
import math

def exec_test(C,F,X):
	v = 2

	if X<=C:
		return " %.7f" % (X/v)

	nbuy = int(math.ceil( (-v*C-C*F+X*F) / (C*F) ))

	print nbuy

	summ = 0
	if nbuy==0: return " %.7f" % (X/v)
	for i in xrange(nbuy):
		summ += C/(v+i*F)
	summ += X/(v+nbuy*F)

	return " %.7f" % summ

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	(C,F,X) = map(lambda x: float(x), nums)
	ret = exec_test(C,F,X)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

