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

class Solution:

	def __init__(self,problem_set=None):
		self.problem = re.split(r'\n',problem_set) 
		cases = int(self.problem.pop(0))
		offset = 0
		lawns = []
		
		for i in range(0,cases):
			
			curr = re.split(r'\s',self.problem[offset].strip())
			y = int(curr[0])
			x = int(curr[1])
			mat = []
			for x in range(0,y):
				vals = re.split(r'\s',self.problem[x+offset+1].strip())
				mat.append([int(i) for i in vals])
			lawns.append(mat)			
			offset = offset + int(y) + 1
			
		
		
		solutions = []
		c=0
		for m in lawns:
			c=c+1
			#if c<>12:
				#continue
				
			solutions.append(self.check_lawn(m,c))
			
		
		self.solutions = solutions
	
	def check_lawn(self,m,case_no):
		
		
		# 1 1 1 2 1 1 2
		# 1 1 1 2 1 1 2
		# 1 1 1 1 1 1 1
		# 1 1 1 1 1 1 1
		# 1 1 1 1 1 1 1
		# 1 1 1 2 1 1 1
		# 1 1 1 1 1 1 1
		# 1 1 1 2 1 1 2
		y = len(m)
		x = len(m[0])
		res = None
		
		for i in range(0,y):
			if res:
				break
			row = m[i]
			mx = max(row)
			col = 0
			for j in range(0,x):
				test = row[j]
				
				if res:
					break
				if test<mx:
					for k in range(0,y):
						if(m[k][col]>test):
							res=True
							break
				col = col + 1
		
		return "YES" if res is None else "NO"
	
	

	
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
	
	
	