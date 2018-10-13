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

def need_time(L, S1, S2, t):
	if L <= S1*t: return (1.0*L/S1, t-1.0*L/S1)
	L -= S1*t
	return (t+1.0*L/S2, 0)

for _t_ in xrange(_T_): 

	#INPUT
	X, S, R, t, N  = (int(x) for x in f.readline().strip().split())
	W = []
	for n in xrange(N):
		B, E, w = (int(x) for x in f.readline().strip().split())
		X -= (E-B)
		W.append((E-B, w))

	if _t_<_t0_ or _t_>=_t1_: continue

	W.sort(key=lambda x:x[1])
	result, t = need_time(X, R, S, t)
	for (l,w) in W:
		dt, t = need_time(l, R+w, S+w, t)
		result+=dt


	#OUTPUT
	if _jid_ < 0: print _t_, result
	g.write(_FMT_ %(_t_+1, str(result)))

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

