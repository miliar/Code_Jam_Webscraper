#! /usr/bin/env python3.2

mapping = {
	'a' : 'y',
	'b' : 'h',
	'c' : 'e',
	'd' : 's',
	'e' : 'o',
	'f' : 'c',
	'g' : 'v',
	'h' : 'x',
	'i' : 'd',
	'j' : 'u',
	'k' : 'i',
	'l' : 'g',
	'm' : 'l',
	'n' : 'b',
	'o' : 'k',
	'p' : 'r',
	'q' : 'z',
	'r' : 't',
	's' : 'n',
	't' : 'w',
	'u' : 'j',
	'v' : 'p',
	'w' : 'f',
	'x' : 'm',
	'y' : 'a',
	'z' : 'q'
}

import sys

if(len(sys.argv) < 2):
	print("Need input file")
	exit(1)
incontent = open(sys.argv[1],'r')

# first line is number of test cases
nbtests = int(incontent.readline())

# for each line, read it and detranslate it
for i in range(nbtests):
	inline = incontent.readline().strip()
	outline = [0] * len(inline)
	for j in range(len(inline)):
		if inline[j] in mapping:
			outline[j] = mapping[inline[j]]
		else:
			outline[j] = inline[j]
	print('Case #' + str(i+1) + ': ' + ''.join(outline))