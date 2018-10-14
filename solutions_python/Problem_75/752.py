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
	case = case.split(' ')

	i = 0
	C = int(case[i])
	C_string = []
	i += 1
	for j in range(C):
		C_string.append(case[i])
		i += 1

	D = int(case[i])
	D_string = []
	i += 1
	for j in range(D):
		D_string.append(case[i])
		i += 1

	N = int(case[i])
	N_string = case[i+1]


	end_string = []
	for char in N_string:
		end_string.append(char)

		if len(end_string) < 2:
			continue

		for c in C_string:
			if (c[0] == char and c[1] == end_string[-2]) or (c[1] == char and c[0] == end_string[-2]):
				end_string = end_string[:-2]
				end_string.append(c[2])
		for d in D_string:
			copy = end_string[:]
			if d[0] in copy:
				copy.remove(d[0])
				if d[1] in copy:
					end_string = []
		
	print_string = '['

	for element in end_string:
		print_string = print_string + element + ', '

	if len(print_string) > 1:
		print_string = print_string[:-2] + ']'
	else:
		print_string = print_string + ']'

	print "Case #"+str(caseNum)+": "+print_string
	caseNum += 1



