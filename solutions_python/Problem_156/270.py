#! /usr/bin/python

import sys
import math

def exec_test(D, Pi):
	print "D=%u Pi=%s" % (D, str(Pi))
	Pi_init = list(Pi)

	step = [max(Pi)]

	for rmmax in xrange(2, max(Pi_init)) :
		Pi = list(Pi_init)
		num=0
		while max(Pi)>=4 :
			i = Pi.index(max(Pi))
			rm = min([rmmax, Pi[i]/2])
			Pi[i] -= rm
			Pi.append(rm)
			num += 1
			step.append(num + max(Pi))
			print step

	return " %u" % min(step)

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	D = int(nums[0])
	nums = fd.readline().split()
	Pi = map(lambda x: int(x), nums)
	assert len(Pi)==D, "Error length"
	ret = exec_test(D, Pi)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

