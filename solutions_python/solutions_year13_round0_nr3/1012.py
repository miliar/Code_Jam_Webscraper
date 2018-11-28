#!/usr/bin/env python

import os
import sys
import getopt
import subprocess
import json
import time
import logging
import time
import errno
import re
import shutil
import uuid
import hashlib

from glob import glob
from pprint import pprint
from copy import deepcopy

def isqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while 1:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
		
class Solution:

	def __init__(self,problem_set=None):
		self.problem = re.split(r'\n',problem_set) 
		cases = int(self.problem.pop(0))
		offset = 0
		solutions = []
		
		for i in range(0,cases):
			
			curr = re.split(r'\s',self.problem[i].strip())
			s = int(curr[0])
			e= int(curr[1])
			sqrs = []
			offset = s
			for x in range(s, e+1):
				test = isqrt(x)
				if test*test == x:
					str_test = str(test)
					str_x = str(x)
					
					if str_x==str_x[::-1] and str_test==str_test[::-1]:
						sqrs.append(test)			
			solutions.append(str(len(sqrs)))
		self.solutions=solutions
	
	def solve(self):
		if not self.problem:
			return None
		final = ""
		case = 1
		for s in self.solutions:
			final += "Case #"+str(case)+": "+s+'\n'
			case += 1
		print final	
		return final.strip()
		
if __name__ == "__main__":	
	
	problem_set="problem.txt"
	solution_set="solution.txt"
	
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'i:o:h', ['in=','out=','h'])
	
	except getopt.GetoptError:
		print "usage: solution.py -i <problem_set_file=default:problem.txt> -o <solution_set_file=default:solution.txt> "
		sys.exit(2)
		
	for opt,arg in opts:
		if opt in ('-h','help'):
			print "usage: solution.py -i <problem_set_file=default:problem.txt> -o <solution_set_file=default:solution.txt> "
			sys.exit(0)
		
		if opt in ('-i','in'):
			problem_set = arg
	
		if opt in ('-o','out'):
			solution_set = arg
			
	problem_set_data = None
	solution_set_data = None
	
	with open(problem_set) as data_file:    
		problem_set_data = data_file.read()
		
	if problem_set_data:	
		solution_set_data = Solution(problem_set_data).solve()
		if solution_set_data:
			f = open(solution_set,'w')
			f.write(solution_set_data)
		else:
			print "Error - no solution!"		
	else:
		print "Error - no problems to solve!"
	
	sys.exit(0)
	
	
	