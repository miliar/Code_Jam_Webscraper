#!usr/bin/python

import re
import sys

fin = open(sys.argv[1], 'r')
fout = open('D:/a.txt', 'w')

r = fin.readline().split(' ')
d = int(r[1])
n = int(r[2])

s = []
for i in range(d):
	s.append(fin.readline().strip())

f = re.compile('\(([a-z]*)\)')
for i in range(n):
	nl = fin.readline().strip()
	nl = f.sub(r'[\1]', nl)
	print nl
	te = re.compile('^'+nl+'$');
	k = 0
	for line in s:
		if te.search(line):
			k += 1;
	fout.write('Case #' + str(i+1) + ': ' + str(k) + '\n')

fin.close()
fout.close()
