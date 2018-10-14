#!/usr/bin/python
import sys
from itertools import combinations 
from copy import copy

def xor_list(a):
	j = 0
	for i in a:
		j ^= int(i)
	return j

def diff_list(a, b):
	c = copy(b)
	for i in a:
		c.remove(i)
	return c

def solve(test_case):
	#print test_case
	valid_list = []
	for i in range(1, len(test_case)):
		for k in combinations(test_case, i):
			if int(xor_list(k)) == int(xor_list(diff_list(k, test_case))):
				#print 'WAT'
				valid_list.append(sum(int(j) for j in k))
			#print k, diff_list(k, test_case), xor_list(k), xor_list(diff_list(k, test_case))
	if len(valid_list) == 0:
		return 'NO'
	return str(max(valid_list))

#Main script---------------------------------------------------------
def main():
	if len(sys.argv) != 2:
		sys.stderr.write("usage: %(self)s 'input'\n"%\
							{'self': sys.argv[0]})
		return

	count = 1
	try:
		f = open(sys.argv[1], 'r')
		for line in f:
			if len(line.split()) == 1:
				continue;
			sys.stdout.write('Case #' + str(count) + ': ' + solve(line.split()) + "\n")
			count += 1
	finally:
		f.close()
		 

if (__name__ == "__main__"):
	main()