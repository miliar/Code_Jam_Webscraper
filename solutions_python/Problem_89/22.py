#!/usr/bin/env python
from math import sqrt

_FMT_ = 'Case #%d: %s\n'
f = open('in','r')
_T_ = int(f.readline())

import sys
if len(sys.argv) > 1:
	_jobs_ = _T_/4
	_jid_ = int(sys.argv[1])
	_t0_ = _jobs_ * _jid_
	_t1_ = _jobs_ *(_jid_+1)
	if _jid_ == 3: _t1_ = _T_
	g = open('out'+str(_jid_),'w')
else:
	_jid_ = -1
	_t0_ = 0
	_t1_ = _T_
	g = open('out','w')

N = []
for _t_ in xrange(_T_): N.append(int(f.readline().strip()))

maxN = max(N)
prime = [True] * (maxN+1)
prime[0] = False
prime[1] = False
pmax = int(sqrt(maxN)) +2
for p in xrange(2,pmax):
	if not prime[p]: continue
	for m in xrange(2, (pmax+1)/p):
		prime[m*p] = False


for _t_ in xrange(_T_): 
	n = N[_t_]
	result = 0
	for p in xrange(2,int(sqrt(n))+2):
		if not prime[p]: continue
		k = 1
		q = p*p
		while q <= n:
			k += 1
			q *= p
		result += (k-1)

	#OUTPUT
	if n== 1: result = 0
	else: result += 1
	if _jid_ < 0: print _t_, result
	g.write(_FMT_ %(_t_+1, str(result)))

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

