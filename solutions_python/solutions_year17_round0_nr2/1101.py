import sys
import os

output_format = 'Case #{0}: {1}\n'

def task2(n):
	s = str(n)
	l = len(s)
	for i in range(l):
		n = task2_helper(n)
	return n

def task2_helper(n):
	s = str(n)
	ret_val = ''
	bigger = False
	l = len(s)
	for i in range(l):
		if (bigger):
			ret_val += '9'
		elif i < l - 1:
			if (s[i]>s[i+1]):
				ret_val += chr(ord(s[i]) - 1)
				bigger = True
			else:
				ret_val += s[i]
		else:
			ret_val += s[i]
	return int(ret_val)

# read the input
file = open(sys.argv[1])
output = open('output.txt', 'w')
lines = file.readlines()
# the number of cases.
T = int(lines[0])
# solve the riddle and write to the output file.

for i in range(T):
	a = int(lines[i+1])
	answer = task2(a)
	output.write(output_format.format(i+1,answer))