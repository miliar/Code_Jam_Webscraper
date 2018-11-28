#!/bin/python

import operator
import sys

dict = {}
dict['a'] = 'y'
dict['o'] = 'e'
dict['z'] = 'q'
dict['q'] = 'z'

a='ejp mysljylc kd kxveddknmc re jsicpdrysi'
b='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
c='de kr kd eoya kw aej tysr re ujdr lkgc jv'

at='our language is impossible to understand'
bt='there are twenty six factorial possibilities'
ct='so it is okay if you want to just give up'

for (char, charp) in zip(a, at):
	dict[char] = charp

for (char, charp) in zip(b, bt):
	dict[char] = charp

for (char, charp) in zip(c, ct):
	dict[char] = charp

#####################################################################

f = open('in.txt', 'r')
out = open('out.txt', 'w')
N = int(f.readline())
for i in xrange(N):
	l = f.readline()
	s = 'Case #'+str(i+1)+": "
	for char in l:
		if char != '\n':
			s += dict[char]
	print s
	out.write(s+"\n")

