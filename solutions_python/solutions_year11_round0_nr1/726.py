#! /usr/bin/python

import sys
import os

filename = sys.argv[1]
f = open(filename, 'r')

file_string = f.read()
file_string = file_string.split('\n')


T = int(file_string[0])
caseNum = 1

for case in file_string[1:] :
		if len(case) <= 1:
				continue
		orange = 1
		blue = 1
		total_time = 0
		diff_time = 0
		last = 'O'
		done = False
		i = 1
		case = case.split(' ')
		while not done:
				num = int(case[i+1])
				col = case[i]
				if 'O' == col:
						diff_loc = abs(num - orange)
						orange = num
				else:
						diff_loc = abs(num - blue)
						blue = num


				if last == col:
						total_time += abs(diff_loc) + 1
						diff_time += abs(diff_loc) + 1
				else:
						if (diff_time <= diff_loc):
								diff_time = abs(diff_loc) + 1 - diff_time
								total_time += diff_time
						else:
								total_time += 1
								diff_time = 1
				
				last = col
				i += 2
				if(i >= len(case)):
					done = True
		print "Case #"+str(caseNum)+": "+str(total_time)
		caseNum += 1



