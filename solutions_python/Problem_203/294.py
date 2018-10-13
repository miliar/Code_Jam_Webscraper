# import sys
# import numpy as np 
# import networkx as nx
# import heapq
# import collections

def import_file(file):
	with open(file) as data:
		T = int(data.readline().rstrip('\n'))

		tests = []
		for i in range(T):
			(R,C) = data.readline().rstrip('\n').split(' ')
			arr = []
			for idx1 in range(int(R)):
				arr.append(list(data.readline().rstrip('\n')))
			tests.append(arr)		
		return (T, tests)

def solution(T):
	length = len(T[0])
	tocopy_row = []
	for row in range(len(T)):
		if T[row].count('?') == length:
			if len(tocopy_row) != 0:
				T[row] = tocopy_row
		else:
			tocopy_row = T[row]

	tocopy_row = []
	for row in reversed(range(len(T))):
		if T[row].count('?') == length:
			if len(tocopy_row) != 0:
				T[row] = tocopy_row
		else:
			tocopy_row = T[row]

	for row in T:
		curr_initial = ''
		for idx1 in range(len(row)):
			if row[idx1] == '?':
				if len(curr_initial) != 0:
					row[idx1] = curr_initial
			else:
				curr_initial = row[idx1]

		for idx1 in reversed(range(len(row))):
			if row[idx1] == '?':
				if len(curr_initial) != 0:
					row[idx1] = curr_initial
			else:
				curr_initial = row[idx1]

	print('')
	for row in T:
		print(''.join(row))

(T, test_cases) = import_file('test.in')
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ': '),
	solution(test)
