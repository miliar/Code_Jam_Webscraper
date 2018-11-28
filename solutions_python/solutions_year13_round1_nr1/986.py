# -*- coding: utf-8 -*-

import sys
import os.path
import os, time, itertools
import math



class Sample:
	def solve(self,r,t):
		b = 2*r-1
		tmp=(-b+math.sqrt(b**2+8*t))/4.0
		print tmp
		ans = math.floor(tmp)				
		return int(ans)

def read_nums():
	return map(int, in_fh.readline().split())
def read_str():
	return in_fh.readline().rstrip('\r\n')

def read_testcase():
	#print board
	#print "-----"
	r,t = read_nums()
	return {'r':r,'t':t}

def read_testcases(test_num):
	for i in range(test_num):
		yield read_testcase()

def wrapper_of_solve(q):
	sample=Sample()
	return sample.solve(**q)

if __name__ == '__main__':

	input_name = sys.argv[1]
	root, ext = os.path.splitext(input_name)
	in_fh=open(input_name)

	test_num=int(in_fh.readline())

	output_name = root + ".out"
	out_fhs=[open(output_name,'w')]

	testcases = read_testcases(test_num)

	mul_iter = itertools.imap(wrapper_of_solve, testcases)

	for (i, r) in enumerate(mul_iter, start=1):
	    for f in out_fhs:
	        print >> f, "Case #%d: %s" % (i, str(r))
