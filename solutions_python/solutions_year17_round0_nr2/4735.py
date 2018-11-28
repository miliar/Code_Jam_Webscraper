#!/usr/bin/env python3

max = 0

def backtrack(n, candidate):
	global max

	if candidate != '0' and int(candidate) > n:
		return
	elif int(candidate) > max:
		max = int(candidate)

	if candidate == '0':
		for i in range(1, 10):
			backtrack(n, candidate + str(i))
	else:
		for i in range(int(candidate[-1]), 10):
			backtrack(n, candidate + str(i))

t = int(input())
for i in range(t):
	n = int(input())
	backtrack(n, '0')

	print('Case #%d: %d' % (i+1, max))
	max = 0
