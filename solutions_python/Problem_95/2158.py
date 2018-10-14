#!/usr/bin/python

import sys

numlines = 0
lines = []
inputs = []
outputs = []

map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c',
 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
 'x': 'm', 'z': 'q', 'q': 'z'}

i=0
for line in sys.stdin.readlines():
	i+=1
	if i is 1:
		numlines = int(line)
	else:
		lines.append(line.strip())
		
for i in range(numlines):
	inputs.append(lines[i])
	
for line in inputs:
	out = ""
	for c in line:
		out += map[c]
	outputs.append(out)

print ("Output",)
i=0
for out in outputs:
	i+=1
	print ("Case #%s: %s" % (i,out),)