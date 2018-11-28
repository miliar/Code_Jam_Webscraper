#!/usr/bin/python

import sys
import re

if len(sys.argv) <= 1:
	sys.exit(0)

f = file(sys.argv[1], 'r')
w = file(sys.argv[1] + '.out', 'w')

lines = f.readlines()
f.close()

controldata = lines[0].rstrip('\n').split(' ')
del lines[0]

L = controldata[0]
D = controldata[1]
N = controldata[2]

words = ""
for i in range(0,int(D)):
	words += lines[0].rstrip('\n') + ' '
	del lines[0]

searchs = []
for line in lines:
	line = line.rstrip('\n')
	searchs.append(re.compile(line.replace('(', '[').replace(')', ']')))

case = 1
for research in searchs:
	result = research.findall(words)
	w.write("Case #%d: %d\n" % (case, len(result)))
	case += 1

w.close()
