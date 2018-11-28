#!/usr/bin/env python
from sys import stdin, stdout
from itertools import *
import multiprocessing
import string

samples = [
		('y qee', 'a zoo'),
		('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
		('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
		('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
		]

mapping = {}
for A,B in samples:
	mapping.update(zip(A,B))

Aset = set(string.lowercase+' ')
Bset = set(string.lowercase+' ')

for k,v in mapping.items():
	Aset.remove(k)
	Bset.remove(v)

mapping.update([(Aset.pop(), Bset.pop())])

def answer(data):
	return ''.join((mapping[x] for x in data))

def cases(s):
	while 1:
		l = s.next().rstrip()
		yield l

if __name__ == '__main__':
	stdin.next()
	p = multiprocessing.Pool(6)
	for n,ans in enumerate(p.map(answer, cases(stdin))):
		print "Case #%d: %s" % (n+1, ans)
