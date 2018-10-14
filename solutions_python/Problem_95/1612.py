#!/usr/bin/python
from re import *

f_in = open("input.txt", "r")
mapping = {}

mapping['a'] = 'y'
mapping['b'] = 'h'
mapping['c'] = 'e'
mapping['d'] = 's'
mapping['e'] = 'o'
mapping['f'] = 'c'
mapping['g'] = 'v'
mapping['h'] = 'x'
mapping['i'] = 'd'
mapping['j'] = 'u'
mapping['k'] = 'i'
mapping['l'] = 'g'
mapping['m'] = 'l'
mapping['n'] = 'b'
mapping['o'] = 'k'
mapping['p'] = 'r'
mapping['q'] = 'z'
mapping['r'] = 't'
mapping['s'] = 'n'
mapping['t'] = 'w'
mapping['u'] = 'j'
mapping['v'] = 'p'
mapping['w'] = 'f'
mapping['x'] = 'm'
mapping['y'] = 'a'
mapping['z'] = 'q'
mapping[' '] = ' '
mapping['\n'] = '\n'

def a(x):
	return mapping[x]

i = 0
for line in f_in:
	if i == 0:
		i += 1
		continue	
	decoded = map(a, line)
	decoded = ''.join(decoded)
	print "Case #" + str(i) + ": " + decoded,
	i += 1
	
