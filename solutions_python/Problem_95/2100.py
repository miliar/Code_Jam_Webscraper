#!/usr/bin/env python

import sys

mapping = {'a': 'y',
		   'b': 'h',
		   'c': 'e',
		   'd': 's',
		   'e': 'o',
		   'f': 'c',
		   'g': 'v',
		   'h': 'x',
		   'i': 'd',
		   'j': 'u',
		   'k': 'i',
		   'l': 'g',
		   'm': 'l',
		   'n': 'b',
		   'o': 'k',
		   'p': 'r',
		   'q': 'z',
		   'r': 't',
		   's': 'n',
		   't': 'w',
		   'u': 'j',
		   'v': 'p',
		   'w': 'f',
		   'x': 'm',
		   'y': 'a',
		   'z': 'q',
		   ' ': ' '}
		   


in_file = open(sys.argv[1], 'r')
num_of_cases = int(in_file.readline())
text_lists = []

for i in xrange(num_of_cases):
	text_lists.append(list(in_file.readline().strip()))

in_file.close()

for i in xrange(len(text_lists)):
	for j in xrange(len(text_lists[i])):
		text_lists[i][j] = mapping[text_lists[i][j]]
		
out_file = open("result.out", 'w')

for i in xrange(num_of_cases):
	out_file.write("Case #" + str(i+1) + ": ")
	out_file.write("".join(text_lists[i]) + '\n')
	
out_file.close()