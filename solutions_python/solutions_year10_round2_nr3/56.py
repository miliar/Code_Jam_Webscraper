#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import math
import os
import os.path

facts = {}
def fact(n):
	if n in facts:
		return facts[n]
	result = math.factorial(n)
	facts[n] = result
	return result

mms = {}
def mm(n,d):
	if d == 0:
		return 1
	if (n,d) in mms:
		return mms[(n,d)]

	result = 0
	for i in itertools.combinations(range(n), d):
		result += 1

	mms[(n,d)] = result
	return result

sps = {}
def sp(n, d):
	#print 'Solving %d with %d' % (n,d)
	if (n,d) in sps:
		return sps[(n,d)]
	result = 0
	assert n <> 1
	if d == 1:
		result = 1
	else:
		for y in xrange(min(d-1,max(1,n-d))):
			#print 'Still solving %d with %d, adding %d' % (n,d,y)
			result += sp(d, d-y-1) * mm(n-d-1, y)
	sps[(n,d)] = result
	#print 'Solved %d with %d: %d' % (n,d, result)
	return result

def solve(n):
	result = 0
	for i in xrange(1, n):
		result += sp(n, i)

	result = result % 100003
	return result

def main():
	for name in os.listdir('.'):
		if name.endswith('.in'):
			result = []
			with open(name) as f:
				for case in xrange(int(f.readline())):
					n = int(f.readline())
					result.append('Case #%d: %d' % (case+1, solve(n)))
			with open('%s.out' % name, 'w') as f:
				f.write('\n'.join(result))
	return 0

if __name__ == '__main__':
	main()
