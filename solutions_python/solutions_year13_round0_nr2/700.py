# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#


import sys

problem = 'B'

# Parse the input file
input_file_name = sys.argv[1]
assert input_file_name[-3:] == '.in', input_file_name

# Parse the output file
output_file_name = sys.argv[2] if len(sys.argv) > 2 else None
if output_file_name:
	assert output_file_name[-4:] == '.out', output_file_name
else:
	output_file_name = problem + '.out'

# Open the input file
input_file = open(input_file_name)

# The output list
output = []

lines = map(str.strip, input_file.readlines())
def read_line(): return lines.pop(0)
def read_parts(): return lines.pop(0).split(' ')
def read_int(): return int(lines.pop(0))
def read_ints(): return map(int, lines.pop(0).split(' '))
def read_float(): return int(lines.pop(0))
def read_floats(): return map(float, lines.pop(0).split(' '))


########## Contest Specific ##########

import math

T = read_int()
assert T >= 1, T
assert T <= 6000, T

while lines:
	N, M = read_ints()
	possible_map = [[False for j in xrange(M)] for i in xrange(N)]
	desired_height = [read_ints() for i in xrange(N)]
	for i in xrange(N):
		row = desired_height[i]
		curr_height = max(row)
		for j in xrange(M):
			h = row[j]
			if h == curr_height:
				possible_map[i][j] = True

	for j in xrange(M):
		col = [desired_height[i][j] for i in xrange(N)]
		curr_height = max(col)
		for i in xrange(N):
			h = col[i]
			if h == curr_height:
				possible_map[i][j] = True

	possible = all([all(possible_map[i]) for i in xrange(N)])

	output.append('YES' if possible else 'NO')


########## Contest Specific End ##########


input_file.close()
print "Closed input file..."

# Write the output
output_file = open(output_file_name, 'w')

cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
print "Closed output file..."