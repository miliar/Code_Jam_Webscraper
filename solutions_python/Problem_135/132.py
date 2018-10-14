#! /usr/bin/python

import sys
import math

def exec_test(r1,C1,r2,C2):
	res = 0;

	l1 = C1[r1-1]
	print l1
	l2 = C2[r2-1]
	print l2
	for i in xrange(4):
		if l1[i] in l2:
			if res==0:
				res=l1[i]
			else:
				res=17
				break
	if res==0:
		res=18


	assert res>=1 and res<=18, ""
	if res==17:
		return " Bad magician!"
	elif res==18:
		return " Volunteer cheated!"
	else:
		return " %i" % res

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	r1 = int(fd.readline().split()[0])
	C1 = [];
	for i in xrange(4):
		nums = fd.readline().split();
		C1.append( map(lambda x: int(x), nums) );
	r2 = int(fd.readline().split()[0])
	C2 = [];
	for i in xrange(4):
		nums = fd.readline().split();
		C2.append( map(lambda x: int(x), nums) );
	ret = exec_test(r1,C1,r2,C2)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

