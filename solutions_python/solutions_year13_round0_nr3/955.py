# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#


import sys

problem = 'C'

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
from math import sqrt

def is_perfect_sqrt(n):
	return sqrt(n) % 1 == 0

def is_fine(n):
	numbers = str(n)
	return (numbers == numbers[::-1])

T = read_int()
assert T >= 1, T
assert T <= 6000, T

while lines:
	fine_and_square = 0
	A, B = read_ints()
	for i in xrange(A, B+1):
		if is_perfect_sqrt(i) and is_fine(i) and is_fine(int(sqrt(i))):
			fine_and_square += 1
			# print i, is_perfect_sqrt(i), sqrt(i)

	output.append(fine_and_square)


########## Contest Specific End ##########


input_file.close()
print "Closed input file..."

# Write the output
output_file = open(output_file_name, 'w')

cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
print "Closed output file..."