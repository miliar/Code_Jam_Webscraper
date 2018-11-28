#!/usr/bin/env python

import sys
import random
import math

DBG = 0

MAXN = 100
MAXA = 100
MAXT = 60

fin = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
fout = sys.stdout

def dbg(s):
	if DBG:
		print >>sys.stdout, '#', s

def iread(n=1):
	while 1:
		s = fin.readline().split()
		if s:
			if n == 1:
				return int(s[0])
			else:
				return tuple(int(x) for x in s)

def sread():
	return fin.readline().split()

def xread():
	n = iread()
	s = [fin.readline().rstrip('\r\n') for i in range(n)]
	return n, s

def tread(n):
	r = []
	for i in range(n):
		a,b = fin.readline().rstrip('\r\n').split()
		a = a.split(':')
		a = int(a[0])*60 + int(a[1]) if len(a)==2 else int(a[0])
		b = b.split(':')
		b = int(b[0])*60 + int(b[1]) if len(b)==2 else int(b[0])
		r.append((a,b))
	#dbg('r=%r' % r)
	return n, r

def cmp(a,b):
	if a[0] < b[0]: return -1
	if a[0] > b[0]: return 1
	return 0

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

def main_a():
	N = iread()
	for n in range(1, N+1):
		ss = xread()
		qq = xread()
		res = get_switches(ss, qq)
		print 'Case #%d: %r' % (n, res)

def tcount(t, a, b):
	na, nb = len(a), len(b)
	i, j = 0, 0
	ca, cb = 0, 0
	at_a, at_b = [], []
	now = 0
	while 1:
		if j == nb or i < na and a[i][0] <= b[j][0]:
			# went from A to B
			if at_a and at_a[0] <= a[i][0]:
				at_a.pop(0)
			else:
				ca += 1
			at_b.append(a[i][1] + t)
			at_b.sort()
			dbg('A->B: %r %d-%d %r %r' % (a[i], ca, cb, at_a, at_b))
			i += 1
		else:
			# went from B to A
			if at_b and at_b[0] <= b[j][0]:
				at_b.pop(0)
			else:
				cb += 1
			at_a.append(b[j][1] + t)
			at_a.sort()
			dbg('A<-B: %r %d-%d %r %r' % (b[j], ca, cb, at_a, at_b))
			j += 1
		if i == na and j == nb:
			break
	return ca, cb

def trains(t, a, b):
	a.sort(key=lambda x: x[0])
	b.sort(key=lambda x: x[0])
	dbg('a=%r b=%r' % (a,b))

	if not a and not b:
		return 0, 0
	if not a:
		return 0, len(b)
	if not b:
		return len(a), 0

	xa, xb = tcount(t, a, b)

	return xa, xb

def main_b():
	N = iread()
	for n in range(1, N+1):
		t = iread()
		dbg('t=%d' % t)
		na,nb = iread(2)
		dbg('na=%d nb=%d' % (na,nb))
		_,a = tread(na)
		_,b = tread(nb)
		res = trains(t, a, b)
		print 'Case #%d: %d %d' % (n, res[0], res[1])

par = '''
1
10
6
1 2 even
3 4 odd
5 6 even
1 4 even
1 6 even
7 10 odd
'''

def pfind(a, n):

	def upd(t, x):
		dbg('t=%r' % t)
		B, E, P = x
		for i in xrange(len(t)):
			b, e, p = t[i]
			if b == B and e == E:
				return p != P
			if e+1 == B: # extend right
				t.append((b, E, p^P))
				break
			elif b-1 == E: # extend left
				t.append((B, e, p^P))
				break
		t.append(x)
		return False

	t = [a[0]]
	for i in xrange(1, n):
		dbg('i=%d'%i)
		if upd(t, a[i]):
			return i
	return n

def do_parity(dat):
	N = int(dat.pop(0))
	for n in xrange(1, N+1):
		a = []
		ln = int(dat.pop(0))
		cnt = int(dat.pop(0))
		for i in xrange(cnt):
			s = dat.pop(0).split()
			a.append((int(s[0]), int(s[1]), s[2]=='odd' and 1 or 0))
		dbg(a)
		if len(a) <= 1:
			res = len(a)
		else:
			res = pfind(a, len(a))
		print 'Case #%d: %d' % (n, res)

def distance(x1,y1,x2,y2):
	r = math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
	#dbg('distance: %r = %f' % ((x1,y1,x2,y2), r))
	return r

MAX_DIST = 1000*1000
MAX_COST = 10.0**200
deep = 0

def do_d():

	def ck_store(items_left, stores_left, cost, i):
		# check price in each store
		store = Stores[i]
		have = set(item for item in store if item not in ('X','Y'))
		dbg('[%d] have=%r' % (i, have))
		min_cost = MAX_COST
		found = 0
		if not have:
			return cost
		x, y = store['X'], store['Y']
		stores_left -= set([i])
		for item in have:
			items_left -= set([item])
			cost += store[item]
			gas = gas_price * distance(x, y, 0, 0)
			c0 = get_cost(items_left, stores_left, cost, 0, 0) + gas
			c1 = get_cost(items_left, stores_left, cost, x, y)
			min_cost = min(min_cost, c0, c1)
		return min_cost

	def get_cost(items_left, stores_left, cost, x0, y0):
		global deep
		deep += 1
		dbg('%d: get_cost: %r' % (deep, [items_left, stores_left, cost, x0, y0]))
		if not items_left:
			# got all items
			gas = gas_price * distance(x0, y0, 0, 0)
			return cost + gas
		min_cost = MAX_COST
		for i in stores_left:
			x, y = Stores[i]['X'], Stores[i]['Y']
			gas = gas_price * distance(x0, y0, x, y)
			new_cost = ck_store(items_left.copy(), stores_left-set([i]), gas+cost, i)
			min_cost = min(min_cost, new_cost)
		return min_cost

	N = iread()
	for n in range(1, N+1):
		num_items, num_stores, gas_price = iread(3)
		it = sread()
		Items = {}
		for x in it:
			i = x.split('!')
			Items[i[0]] = len(i) > 1 # true if perishable !
		dbg('Items=%r' % Items)
		all_items = set(i for i in Items.keys())
		Stores = []
		for i in range(num_stores):
			st = sread()
			store = { 'X': int(st[0]), 'Y': int(st[1]) }
			#distance(0,0,store['X'],store['Y'])
			for x in st[2:]:
				i,p = x.split(':')
				store[i] = int(p)
			Stores.append(store)
		dbg('Stores=%r' % Stores)
		all_stores = set(range(len(Stores)))
		res = get_cost(all_items, all_stores, 0, 0, 0)
		print 'Case #%d: %.07f' % (n, res)

#gen_data()
#test()
#main_b()
#do_parity(par.strip().split('\n'))
#do_d()

def ca():
	N = iread()
	for n in range(1, N+1):
		P,K,L = iread(3)
		F = iread(2)
		freq = []
		for x in F:
			freq.append(x)
		dbg('%d,%d,%d: %r' % (P,K,L, F))
		if P*K < L:
			print 'Case #%d: Impossible' % n
			continue
		# build freq
		freq = sorted(freq)
		freq.reverse()
		#print freq
		r = []
		for k in xrange(K):
			r.append([])
		for p in xrange(P):
			for k in xrange(K):
				if not freq: break
				r[k].append(freq.pop(0))
		res = 0
		for k in xrange(K):
			m = 1
			for f in r[k]:
				res += f*m
				m += 1

		print 'Case #%d: %d' % (n, res)

ca()
