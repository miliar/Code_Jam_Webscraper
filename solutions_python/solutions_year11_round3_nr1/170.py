#!/usr/bin/env python

import operator
import math
from pprint import pprint
from fractions import gcd

log = False
def solve(picture):
	red_pic = list(picture)
	
	for i, row in enumerate(picture[:-1]):
		for j, e in enumerate(row[:-1]):
			if e == '#':
				if red_pic[i+1][j] == '#' and red_pic[i][j+1] == '#' and red_pic[i+1][j+1] == '#':
					red_pic[i][j] = '/'
					red_pic[i+1][j] = '\\'
					red_pic[i][j+1] = '\\'
					red_pic[i+1][j+1] = '/'
	
	for i, row in enumerate(red_pic):
		for j, e in enumerate(row):
			if e=='#':
				return
				
	#~ if any([i=='#' for i in row] for row in red_pic):
		#~ if log:
			#~ print red_pic
		#~ return 'Impossible'
		
	return red_pic
			
					
WHILE = '.'
BLUE = '#'

BLUE_SIZE = 1
RED_SIZE = 2
	
if __name__ == '__main__':    
	with open('A-large-0.in') as f:
		lines = f.readlines()

	problems = []
	line_num = 0
	
	T = int(lines[line_num])
	line_num += 1
	
	for _ in range(T):
		R, C = map(int, lines[line_num].split())
		line_num += 1
		
		picture = []
		for Ri in range(R):
			row = list(lines[line_num].strip())
			line_num += 1
			
			picture.append(row)
				

		problems.append(picture)

	if log:
		pprint(problems)

	for problem_num, picture in enumerate(problems):
		if log:
			print '###'
			print picture
		
		answer = solve(picture)
		
		print 'Case #%s:' % (problem_num+1)
		if answer:
			for row in answer:
				print "".join(row)
		else:
			print 'Impossible'




