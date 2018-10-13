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
	N, PD, PG  = (int(x) for x in f.readline().strip().split())


	if _t_<_t0_ or _t_>=_t1_: continue

	#TODO ----------------------------------------------
	if PG==0:
		if PD!=0: result = 'Broken'
		else: result = 'Possible'
	elif PG==100:
		if PD!=100: result = 'Broken'
		else: result = 'Possible'
	elif N>=100: result = 'Possible'
	else:
		for n in xrange(1,N+1):
			if (n*PD) % 100 == 0:
				result = 'Possible'
				break
		else: result = 'Broken'

	#OUTPUT
	if _jid_ < 0: print _t_, result
	g.write(_FMT_ %(_t_+1, str(result)))

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

