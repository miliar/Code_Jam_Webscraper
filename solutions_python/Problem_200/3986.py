#!/bin/python

import sys

num_cases = int(raw_input())

def printResult(i, res):
	print "Case #{}: {}".format(i+1, res)

def digitList(n):
	return map(int, str(n))

def trim(digs):
	for i in range(len(digs)):
		if digs[i] > 0:
			return digs[i:]

def intFromDigits(digs):
	return int(''.join(map(str, trim(digs))))

def isTidy(n):
	n_list = digitList(n)
	for d in range(len(n_list) - 1):
		if n_list[d+1] < n_list[d]:
			return False
	return True

def lastTidyNum(N):
	ind = len(digitList(N)) - 1
	while (not isTidy(N)):
		n_list = digitList(N)

		n_list[ind] = 9

		ind2 = ind-1
		n_list[ind2] = n_list[ind2] - 1
		while ind2 >= 0 and n_list[ind2] < 0:
			n_list[ind2] = 9
			n_list[ind2 - 1] = n_list[ind2 - 1] - 1
			ind2 = ind2 - 1

		N = intFromDigits(trim(n_list))
		ind = ind - 1
	return N

for i in range(num_cases):
	n = int(raw_input())
	printResult(i,lastTidyNum(n))
