#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def f(n):
	'''テストサンプル

	>>> f(1)
	2
	>>> f(2)
	3
	'''
	return n+1

def check_intersection(wireA,wireB):
	'''交点があるかチェック

	>>> check_intersection((1,10),(5,5))
	True
	>>> check_intersection((5,5),(7,7))
	False
	'''
	if wireA[0] > wireB[0]:
		wireA,wireB = wireB,wireA
	if not wireA[0] < wireB[0]:
		raise
	if wireA[1] < wireB[1]:
		return False
	else:
		return True

def count_intersection(wires):
	'''交点を数える

	>>> count_intersection([(1, 10), (5, 5), (7, 7)])
	2
	>>> count_intersection([(1, 1), (2, 2)])
	0
	'''
	intersection_number = 0
	for i in xrange(1,len(wires)):
		for j in xrange(0,i):
			if check_intersection(wires[i],wires[j]):
				intersection_number += 1
	return intersection_number

def main():
	test_case_count = int(sys.stdin.readline())
	for test_case_number in xrange(1,test_case_count+1):
		wire_count = int(sys.stdin.readline())
		wires = []
		for i in xrange(0,wire_count):
			(A,B) = sys.stdin.readline().split()
			wires.append((int(A),int(B)))
		intersection_number = count_intersection(wires)
		print 'Case #'+str(test_case_number)+': '+str(intersection_number)

def test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	main()

