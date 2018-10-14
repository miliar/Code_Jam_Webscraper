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
		self.problem.pop(0)
		games = []
		curr = 0
		for i in self.problem:
			row = i
			if row.strip()=='':
				curr = curr + 1
				continue
			if len(games)-1 < curr:
				games.append([])
				
			games[curr].extend(row)
		
		solutions = []
		for g in games:
			state = 'Draw'
			for p in g:
				if p=='.':
					state = "Game has not completed"
			
			
			check = 'X'
			if ( (g[0]==check or g[0]=='T') and (g[1]==check or g[1]=='T') and (g[2]==check or g[2]=='T') and (g[3]==check or g[3]=='T') ) or \
				( (g[4]==check or g[4]=='T') and (g[5]==check or g[5]=='T') and (g[6]==check or g[6]=='T') and (g[7]==check or g[7]=='T') ) or \
				( (g[8]==check or g[8]=='T') and (g[9]==check or g[9]=='T') and (g[10]==check or g[10]=='T') and (g[11]==check or g[11]=='T') ) or \
				( (g[12]==check or g[12]=='T') and (g[13]==check or g[13]=='T') and (g[14]==check or g[14]=='T') and (g[15]==check or g[15]=='T') ) or \
				( (g[0]==check or g[0]=='T') and (g[4]==check or g[4]=='T') and (g[8]==check or g[8]=='T') and (g[12]==check or g[12]=='T') ) or \
				( (g[1]==check or g[1]=='T') and (g[5]==check or g[5]=='T') and (g[9]==check or g[9]=='T') and (g[13]==check or g[13]=='T') ) or \
				( (g[2]==check or g[2]=='T') and (g[6]==check or g[6]=='T') and (g[10]==check or g[10]=='T') and (g[14]==check or g[14]=='T') ) or \
				( (g[3]==check or g[3]=='T') and (g[7]==check or g[7]=='T') and (g[11]==check or g[11]=='T') and (g[15]==check or g[15]=='T') ) or \
				( (g[0]==check or g[0]=='T') and (g[5]==check or g[5]=='T') and (g[10]==check or g[10]=='T') and (g[15]==check or g[15]=='T') ) or \
				( (g[3]==check or g[3]=='T') and (g[6]==check or g[6]=='T') and (g[9]==check or g[9]=='T') and (g[12]==check or g[12]=='T') ) :
				state = "X won"
			
			if state is not "X won":
				check = 'O'
				if ( (g[0]==check or g[0]=='T') and (g[1]==check or g[1]=='T') and (g[2]==check or g[2]=='T') and (g[3]==check or g[3]=='T') ) or \
					( (g[4]==check or g[4]=='T') and (g[5]==check or g[5]=='T') and (g[6]==check or g[6]=='T') and (g[7]==check or g[7]=='T') ) or \
					( (g[8]==check or g[8]=='T') and (g[9]==check or g[9]=='T') and (g[10]==check or g[10]=='T') and (g[11]==check or g[11]=='T') ) or \
					( (g[12]==check or g[12]=='T') and (g[13]==check or g[13]=='T') and (g[14]==check or g[14]=='T') and (g[15]==check or g[15]=='T') ) or  \
					( (g[0]==check or g[0]=='T') and (g[4]==check or g[4]=='T') and (g[8]==check or g[8]=='T') and (g[12]==check or g[12]=='T') ) or \
					( (g[1]==check or g[1]=='T') and (g[5]==check or g[5]=='T') and (g[9]==check or g[9]=='T') and (g[13]==check or g[13]=='T') ) or \
					( (g[2]==check or g[2]=='T') and (g[6]==check or g[6]=='T') and (g[10]==check or g[10]=='T') and (g[14]==check or g[14]=='T') ) or \
					( (g[3]==check or g[3]=='T') and (g[7]==check or g[7]=='T') and (g[11]==check or g[11]=='T') and (g[15]==check or g[15]=='T') ) or \
					( (g[0]==check or g[0]=='T') and (g[5]==check or g[5]=='T') and (g[10]==check or g[10]=='T') and (g[15]==check or g[15]=='T') ) or \
					( (g[3]==check or g[3]=='T') and (g[6]==check or g[6]=='T') and (g[9]==check or g[9]=='T') and (g[12]==check or g[12]=='T') ) :
					state = 'O won'
					
			solutions.append(state)
		self.solutions = solutions
		
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
	
	
	