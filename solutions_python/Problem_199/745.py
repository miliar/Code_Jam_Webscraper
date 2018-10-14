#!/bin/usr/env python

t = int(raw_input())

swap = {'-':'+', '+':'-'}

for tn in range(t):
	k, s = raw_input().split(' ')
	s = int(s)
	k = list(k)
	output = 0
	size = len(k)
	i = 0
	while i <= size - s:
		if k[i] == '-':
			j = 0
			flag = 1
			while j < s:
				k[i + j] = swap[k[i + j]]
				if k[i + j] == '-' and flag:
					flag = 0
					jump = i + j - 1
				j += 1
			if not flag:
				i = jump
			output += 1
		i += 1
	while i < size:
		if k[i] == '-':
			output = 'IMPOSSIBLE'
			break
		i += 1
	print("Case #" + str(tn + 1) + ": " + str(output))
