#!/usr/bin/python
import string

def input(name):
	with open(name) as f:
		n = int(f.readline().strip())
		for i in xrange(n):
			yield f.readline().strip()

def mapping():
	a = ('ejp mysljylc kd kxveddknmc re jsicpdrysi'
		'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
		'de kr kd eoya kw aej tysr re ujdr lkgc jvqz')

	b = ('our language is impossible to understand'
		'there are twenty six factorial possibilities'
		'so it is okay if you want to just give upzq')

	return string.maketrans(a,b)

def solve(m, t):
	return t.translate(m)

def output(results):
	with open('out', 'w') as f:
		for i, result in enumerate(results):
			f.write('Case #%d: %s\n' % (i+1, result))

if __name__ == '__main__':
	results = []
	m = mapping()
	for i in input('in'):
		results.append(solve(m, i))
	output(results)

