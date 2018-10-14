#!/usr/bin/env python2

import sys

import multiprocessing

inp = iter(sys.stdin)

n = int(next(inp))

instances = []
for i in range(n):
	k = int(next(inp))
	pi = []
	for j in range(k):
		pi.append(next(inp).rstrip())
	instances.append(pi)


def solve(p):
	p = [s.split(" ") for s in p]

	w = set()
	for s in p:
		w |= set(s)
	dic = {x: i for i, x in enumerate(w)}

	p = [[dic[w] for w in s] for s in p]

	fw = set(p[0])
	ew = set(p[1])

	def do(l, fw, ew):
		if len(l) == 0:
			return len(fw & ew)
		else:
			fst = l[0]
			rst = l[1:]
			w = set(fst)
			return min(do(rst, fw | w, ew),
					   do(rst, fw, ew | w))
	o = do(p[2:], fw, ew)
	return o


pool = multiprocessing.Pool()
for k, o in enumerate(pool.map(solve, instances)):
	print "Case %d: %d" % (k+1, o)
