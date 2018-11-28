#!/usr/bin/python
from __future__ import with_statement
import sys

def solve_problem(input_file):
		
	with open(input_file, 'r') as rf:
		count=int(rf.readline())

		#print count	
		for idx in range(0, count):
			#print idx
			line = rf.readline().strip('\n')
			#print line	
			numbers = {}
			actual = 0
			for c in line:
				if not c in numbers:
					if actual == 0:
						numbers[c]=1

					elif actual == 1:
						numbers[c]=0
					else:
						numbers[c] =actual
					actual+=1
			if actual == 1:
				actual=2

			#print	actual
			seconds = 0
			
			for c in line:
				seconds *= actual
				seconds += numbers[c]
			#print seconds
			print "Case #%d: %d" % (idx+1, seconds)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		solve_problem(sys.argv[1])
	else:
		print 'enter input file as first paramater'
