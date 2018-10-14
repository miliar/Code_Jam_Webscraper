#!/usr/bin/env python

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

for _t_ in xrange(_T_): 

	#INPUT
	tokens  = [int(x) for x in f.readline().strip().split()]
	N = tokens[0]
	S = tokens[1]
	p = tokens[2]
	n = tokens[3:]


	if _t_<_t0_ or _t_>=_t1_: continue

	#TODO ----------------------------------------------
	result = 0
	P1 = 3*p - 4
	P2 = 3*p - 2
	for i in n:
		if i < P1: continue
		if i >= P2:
			result += 1
			continue
		if S > 0 and i >= p:
			result += 1
			S -= 1

	#OUTPUT
	if _jid_ < 0: print _t_, result
	g.write(_FMT_ %(_t_+1, str(result)))

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

