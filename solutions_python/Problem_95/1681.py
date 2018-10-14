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

mapping = {}
mapping['q']='z'
mapping['z']='q'
f1 = open('in1','r')
f2 = open('in2','r')
for line in f1.readlines():
	target = f2.readline()
	for i in xrange(len(line)):
		ch = line[i]
		if 'a' <= ch  <= 'z':
			mapping[ch] = target[i+9]

for _t_ in xrange(_T_): 

	#INPUT
	line = f.readline().strip()


	if _t_<_t0_ or _t_>=_t1_: continue

	#TODO ----------------------------------------------
	res =[] 
	for i in xrange(len(line)):
		ch = line[i]
		if 'a' <= ch <= 'z':
			res.append(mapping[ch])
		else:
			res.append(ch)
	result = ''.join(res)
	


	#OUTPUT
	if _jid_ < 0: print _t_, result
	g.write(_FMT_ %(_t_+1, result))

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

