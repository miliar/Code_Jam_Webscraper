#!/usr/bin/env python

import string

tr = string.maketrans('ynficwlbkuomxsevzpdrjgthaq', 'abcdefghijklmnopqrstuvwxyz')

linenum = raw_input()

result = []

for i in range(1, int(linenum)+1):
	line = raw_input()
	lineConverted = line.translate(tr)
	result.append("Case #" + str(i) + ": " + lineConverted)

for str in result:
	print str
