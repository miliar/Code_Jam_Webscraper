#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import ceil

def f(n):
	'''テストサンプル

	>>> f(1)
	2
	>>> f(2)
	3
	'''
	return n+1

def div_with_ceil(a,b):
	return int(ceil(float(a)/b))

def count_load_tests(L,P,C):
	'''
	>>> count_load_tests(50,700,2)
	2
	>>> count_load_tests(19,57,3)
	0
	>>> count_load_tests(1,1000,2)
	4
	>>> count_load_tests(24,97,2)
	2
	'''
	test_point = 0
	i = div_with_ceil(P,C)
	while L < i:
		test_point += 1
		i = div_with_ceil(i,C)
	count = 0
	while 2 ** count <= test_point:
		count += 1
	return count
	
def main():
	test_case_count = int(sys.stdin.readline())
	for test_case_number in xrange(1,test_case_count+1):
		(L,P,C) = sys.stdin.readline().split()
		number_of_load_tests = count_load_tests(int(L),int(P),int(C))
		print 'Case #'+str(test_case_number)+': '+str(number_of_load_tests)

def test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
#	test()
	main()

