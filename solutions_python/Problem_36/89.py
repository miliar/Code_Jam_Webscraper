#!usr/bin/python

import sys

fin = open(sys.argv[1], 'r')
fout = open('E:/gcj2009/c.txt', 'w')

class Map:
	def __init__(self):
		self.d = {}
	def add(self, c, pos):
		if not self.d.has_key(c):
			self.d[c] = []
		self.d[c].append(pos)

map = Map()
str = "welcome to code jam"
for i in range(19):
	map.add(str[i], i+1)

n = int(fin.readline())

for i in range(n):
	s = [0 for j in range(20)]
	s[0] = 1
	l = fin.readline().strip()
	for c in l:
		if not map.d.has_key(c):
			continue
		for j in map.d[c]:
			s[j] = (s[j]+s[j-1])%10000
	fout.write('Case #' + repr(i+1) + ': ')
	fout.write('%04d'%s[19] + '\n') # the last
