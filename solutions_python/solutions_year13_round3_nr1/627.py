#!/usr/bin/env python3

import sys

VOWELS = ['a', 'e', 'i', 'o', 'u']

def count_consonantes(name):
	max_count, count = 0, 0
	index = 0
	#print('Evaluating', name)
	while index < len(name):
		if name[index] not in VOWELS:
			count = count + 1
			#print('More cons', count)
		else:
			max_count = max(count, max_count)
			count = 0
		index = index + 1
	max_count = max(max_count, count)
	#print('Conson', max_count)
	return max_count

def count_cons(name, i, n):
	num = 0
	#print('Substring size', i)
	for j in range(0, len(name) - i + 1):
		c = count_consonantes(name[j:j+i])
		if c >= n:
			#print('Found n-value')
			num = num + 1
	return num

def magic(name, n):
	num = 0
	for i in range(n, len(name) + 1):
		c = count_cons(name, i, n)
		num = num + c
	return num

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(ncases):
		name, n = sys.stdin.readline().strip().split(' ')
		n = int(n)
		nvalues = magic(name, n)
		print('Case #', case + 1, ': ', nvalues, sep='')
