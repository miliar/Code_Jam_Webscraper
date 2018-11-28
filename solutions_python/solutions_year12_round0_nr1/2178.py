#!/usr/bin/python3.1

import operator

'qz'
mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
lines = open('a.txt').readlines()
i = 1
for line in lines[1:]:
	print('Case #' + str(i) + ': ', end='')
	i += 1
	for c in line:
		if c in mapping: c = mapping[c]
		print(c, end='')
