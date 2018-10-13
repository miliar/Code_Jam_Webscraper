#! /usr/bin/python

import sys
import math

def exec_test(X,R,C):

	#Trivial loosing cases
	# XXX
	# X X <- Impossible to fill the center
	# XX
	if X>=7:
		return " RICHARD"
	# XXXXXXXX <- Impossible to fit in either direction
	if X>max(R,C):
		return " RICHARD"
	# L shaped format with both direction strictely longer that min(R,C)
	if X>=2*min(R,C)+1:
		return " RICHARD"
	# If place the X-omino will leave not multiple of X
	if (R*C)%X!=0:
		return " RICHARD"

	#Trivial winning cases
	if X<=3:
		return " GABRIEL"

	if X==4:
		if min(R,C)>=3:
			return " GABRIEL"
		assert min(R,C)==2, "ERROR"
		return " RICHARD"
	elif X==5:
		if min(R,C)==2:
			return " RICHARD"
		if min(R,C)>=4:
			return " GABRIEL"
		assert min(R,C)==3, "ERROR"
		if max(R,C)>=7:
			return " GABRIEL"
	elif X==6:
		assert min(R,C)>=3, "ERROR"
		if min(R,C)==3:
			return " RICHARD"
		if min(R,C)>=4:
			return " GABRIEL"

	return " FAIL"

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	assert len(nums)==3, "Error input"
	(X,R,C) = map(lambda x: int(x), nums)
	ret = exec_test(X,R,C)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

