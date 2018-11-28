#!/usr/bin/python

from sys import stdin, stdout

d = {}

w = open('example').readlines()

for i in xrange(0, len(w), 2):
	for j in xrange(len(w[i])):
		if (w[i][j].isalpha()):
			d[w[i][j]] = w[i+1][j]
d['q'] = 'z'
d['z'] = 'q'

ww = stdin.readlines()
for i in range(len(ww)):
	stdout.write('Case #%d: ' % (i, ) + ''.join(map(lambda x: d[x] if x.isalpha() else x, ww[i])))
