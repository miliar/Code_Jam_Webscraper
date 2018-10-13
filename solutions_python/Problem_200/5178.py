import numpy as np
import sys

def n_to_arr(n):
	return list( map(int, list(str(n)) ) )

def is_tidy(n_arr):
	return (sorted(n_arr) == n_arr)

def tidy_bf(n):
	while not is_tidy(n_to_arr(n)):
		n -= 1
	return n
		
ns = []
nums = 0
with open('B-small-attempt1.in', 'r') as infile:
	nums = int(infile.readline())
	for i in range(nums):
		ns.append(tidy_bf(int(infile.readline())))

f = open('B-small-attempt1.out', 'w')
for i in range(nums):
	strout = 'Case #' + str(i+1) + ': ' + str(ns[i])  + '\n'
	f.write(strout)
f.close()