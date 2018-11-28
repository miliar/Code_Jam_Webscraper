#! /usr/bin/env python3.2

import sys
	
def get_nb_digits(i):
	"""
		pre:  1 <= i
		post: i unchanged & returns the number of digits of i
	"""
	count = 0
	while i > 0:
		i = i // 10
		count = count + 1
	return count
	
def get_nb_recycling_sibling(a,b,d):
	"""
		pre:  1 <= a <= b, d & d is the number of digits of a
		post: a,b,d unchanged &
			  returns the number of numbers that forms a recycled pair with a
			  and that are smaller or equal to b
	"""
	nbs = set()
	recycling = False
	m = a
	for i in range(d):
		m = m + (m % 10) * 10**d
		m = m // 10
		if m > a and m <= b:
			nbs.add(m)
		if m == a:
			recycling = True
	if recycling:
		return len(nbs)
	else:
		return 0
	
def count_recycled_pairs(a,b):
	"""
		pre:  1 <= a <= b
		post: a,b unchanged & returns the number of recycled pairs between
			  a and b, inclusive
	"""
	d = get_nb_digits(a)
	count = 0
	for i in range(a,b):
		count = count + get_nb_recycling_sibling(i,b,d)
	return count
	

if(len(sys.argv) < 2):
	print("Need input file")
	exit(1)
incontent = open(sys.argv[1],'r')

# first line is number of test cases
nbtests = int(incontent.readline())

# for each line, read it and compute it
for i in range(nbtests):
	inline = incontent.readline().strip()
	inline = inline.split()
	a = int(inline[0])
	b = int(inline[1])
	print('Case #' + str(i+1) + ': ' + str(count_recycled_pairs(a,b)))