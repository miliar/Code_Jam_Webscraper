from __future__ import with_statement
from contextlib import nested
import sys
from time import time

Inf = 10**5

class node0(object):
	def __init__(self, GI, C = None):
		if C is None:
			self.I = 0 if GI == 0 else Inf
		else:
			self.G = GI
			self.C = C
	def calc(self, child1, child2):
		val = (child1.I + child2.I), min(child1.I, child2.I)
		self.I = val[self.G]
		if self.C:
			self.I = min(self.I, min(val) + 1)

class node1(object):
	def __init__(self, GI, C = None):
		if C is None:
			self.I = 0 if GI == 1 else Inf
		else:
			self.G = GI
			self.C = C
	def calc(self, child1, child2):
		val = min(child1.I, child2.I), (child1.I + child2.I)
		self.I = val[self.G]
		if self.C:
			self.I = min(self.I, min(val) + 1)

nodes = node0, node1

def do_case(fit):
	M, V = map(int, fit.next().split(' '))
	node = nodes[V]
	T = [node(*map(int, fit.next().split(' '))) for i in xrange(M)]
	for i in xrange((M-1)//2 - 1, -1, -1):
		T[i].calc(T[i*2+1], T[i*2+2])
	return T[0].I if T[0].I < Inf else 'IMPOSSIBLE'
	

def do_all(fin, fout):
	start = time()
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %s\n" % (i, do_case(fit)))
	print "Execution time:", time() - start

use_psyco = True

if __name__ == '__main__':
	if use_psyco:
		try:
			import psyco
			psyco.full()
			print "Optimized with Psyco"
		except ImportError:
			pass
	do_all(*sys.argv[1:3])
