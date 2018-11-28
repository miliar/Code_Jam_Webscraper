#!/usr/bin/env python
from sys import stdin
from itertools import *
from collections import defaultdict

def answer(data):
	comL, desL, invL = data

	com = {}
	for e1,e2,e3 in comL:
		com[ (e1, e2) ] = com[ (e2, e1) ] = e3

	des = defaultdict(set)
	for e1,e2 in desL:
		des[e1].add(e2)
		des[e2].add(e1)

	contents = defaultdict(int)
	result = [ invL[0] ]
	contents[invL[0]] = 1

	for inv in invL[1:]:
		result.append(inv)
		contents[inv] += 1
		while len(result) > 1 and com.has_key(tuple(result[-2:])):
			key = tuple(result[-2:])
			for x in xrange(2):
				contents[result[-1]] -= 1
				result.pop()
			after = com[key]
			result.append(after)
			contents[after] += 1
			continue

		if len(result) > 1:
			for opE in des[result[-1]]: 
				if contents[opE] > 0:
					result = []
					contents = defaultdict(int)

	return "[%s]" % ", ".join(result)

def cases(s):
	while 1:
		pci = iter(stdin.next().split())
		C = int(pci.next())
		com = list(islice(pci, C))
		D = int(pci.next())
		des = list(islice(pci, D))
		pci.next()
		inv = pci.next()
		yield (com, des, inv)

if __name__ == '__main__':
	stdin.next()
	for n,case in enumerate(cases(stdin)):
		print "Case #%d: %s" % (n+1, answer(case))
