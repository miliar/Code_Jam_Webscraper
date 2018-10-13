#!/usr/bin/env python

import sys
import random

DBG = 0

MAXN = 20
MAXS = 100
MAXQ = 1000
NAMELEN = 100

fin = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
fout = sys.stdout

def dbg(s):
	if DBG:
		print >>sys.stdout, '#', s

def iread():
	while 1:
		s = fin.readline().split()
		if s:
			return int(s[0])

def xread():
	n = iread()
	# should i ignore trailing spaces?
	return [fin.readline().rstrip('\r\n') for i in range(n)]

def get_switches(ss, qq=None):
	if not qq and type(ss) == tuple:
		ss, qq = ss
	ss, qq = set(ss), list(qq)
	dbg('s=%r\n  q=%r' % (list(ss), qq))

	if not qq:
		# no queries
		return 0
	if ss - set(qq):
		dbg('zero: %r' % list(ss-set(qq)))
		return 0

	n = 0
	ls = []
	dist = set()
	for q in qq:
		if q in ss:
			# don't count a query that is not a name of any SE
			dist.add(q)
		if len(dist) == len(ss):
			dbg('[%d] %s: %r' % (n, q, ls))
			n += 1
			ls = []
			dist = set()
			if q in ss:
				dist.add(q)
		ls.append(q)
	if DBG:
		rest = ss - dist
		dbg('[%d] %s: %r' % (n, rest.pop(), ls))

	return n

def rnd(ns=2, nq=5):
	a = [chr(x) for x in range(ord('a'), ord('z')+1)]
	s = [random.choice(a) for x in range(ns)]
	if nq is None:
		return s
	q = [random.choice(s) for x in range(nq)]
	return s, q

def test():
	if 0:
		assert 1 == get_switches('cab', 'cababaa')
		assert 1 == get_switches('dcab', 'dcababaa')
		assert 0 == get_switches('abc', 'ababaa')
		assert 4 == get_switches('ab', 'ababaaq')
		assert 4 == get_switches('ab', 'aqbqabaaq')
		assert 1 == get_switches('cab', 'ccacbabaa')
		assert 2 == get_switches('cab', 'ccacbabaac')
		assert 1 == get_switches('cab', 'cccbaaac')
	for i in range(MAXN):
		get_switches(rnd(MAXS, MAXQ))

def gen_data():
	print MAXN
	for i in range(MAXN):
		s, q = rnd(MAXS, MAXQ)
		print len(s)
		for x in s: print x
		print len(q)
		for x in q: print x

def main():
	N = iread()
	for n in range(1, N+1):
		ss = xread()
		qq = xread()
		res = get_switches(ss, qq)
		print 'Case #%d: %r' % (n, res)

#gen_data()
#test()
main()
