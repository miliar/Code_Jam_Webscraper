#!/usr/bin/python
from __future__ import with_statement
import sys

def extract(case):
	#print case
	res = [];
	mode = 0
	for i in case:
		if mode == 0:
			if i == '(':
				mode = 1
				chunk = ''
				continue
			else:
				res += [i]
		if mode == 1:
			if i == ')':
				mode = 0;
				res += [chunk]
				continue
			else:
				chunk += i
	return res		
			

def solve_problem(input_file):
	with open(input_file, 'r') as rf:
		ldn=rf.readline().split();
		#print ldn
			
		index = {}

		for i in range(0, int(ldn[1])):
			word = rf.readline().strip('\n')
			#print word
			pom = index
			for char in word:
				if not char in pom:
					pom[char] = {}
				pom = pom[char] 
			
		
			
		
		idx = 0	
		for i in range(0, int(ldn[2])):
			idx+=1
			case = rf.readline().strip('\n')
			res = extract(case) 
			if not len(res) == int(ldn[0]):
				print "COUNT doesn't match"
				return 
			
			level = []
			level = [index]
			 
			#print level	
			for chunk in res:
				pom_level = []
				for i in chunk: 
					for j in level:
						if i in j:
							pom_level += [j[i]]
				#print "-----------------", pom_level
				if len(pom_level) == 0:
				 	break
				else: 
					level = pom_level

			print "Case #%d: %d" % (idx, len(pom_level))

if __name__ == '__main__':
	if len(sys.argv) == 2:
		solve_problem(sys.argv[1])
	else:
		print 'enter input file as first paramater'
