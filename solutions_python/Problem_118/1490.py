# -*- coding: utf-8 -*-

import sys
import os.path
import os, time, itertools

UPPER_HEIGHT=2
LOWER_HEIGHT=1
INITIAL_HEIGHT=100

class Sample:
	def solve(self,lower,upper):
		num=0
		
		for i in range(lower,upper+1):
			if self.judge_parindromeness(i):
				root = self.judge_squareness(i)
				if root is not None and self.judge_parindromeness(root):
					num += 1
		
		return num

	def judge_parindromeness(self,n):
		return str(n)==str(n)[::-1]

	def judge_squareness(self,n):
	    m = int(n**.5)
	    return m if abs(m*m - n) < 1e-6 else None

	def judge(self,row_size,col_size):
		return True

def read_nums():
	return map(int, in_fh.readline().split())
def read_str():
	return in_fh.readline().rstrip('\r\n')

def read_testcase():
	lower,upper = read_nums()
	return {'lower':lower,'upper':upper}

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
