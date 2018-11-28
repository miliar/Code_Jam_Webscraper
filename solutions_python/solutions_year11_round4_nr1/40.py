#!/usr/local/bin/python2.7
#coding=UTF-8

# Copyright © 2009-2011 by T. Chan.

# Reading start: 
# Code start:    
# Test pass:     
# Small dl:      
# Small run:     
# Small accept:  
# Large dl:      
# Large run:     
# Large submit:  
# Complete:      


from __future__ import division
#from __future__ import absolute_import,with_statement
#from __future__ import print_function
import __builtin__,sys,os,os.path,re,time,StringIO as io
import operator,array,itertools,bisect
import pprint,pdb,traceback,warnings
from pdb import set_trace as debug
from math import hypot,pi,sin,cos,tan,sqrt,floor,ceil,asin
from itertools import islice,izip,imap
try:
	import collections
	from collections import namedtuple
except: pass
try: from math import fsum
except: warnings.warn("math.fsum() not supported; aliasing it to sum"); fsum = sum
if not 'set' in __builtin__.__dict__: from sets import Set as set,ImmutableSet as frozenset

def process3(X,S,accum):
	ret = {}
	accum.sort()
	prev = 0
	for B,E,w in accum:
		w += S
		assert B >= prev
		prev = E
		dist = E-B
		ret[w] = ret.get(w,0)+dist
		X -= dist
	assert S not in ret
	ret[S] = X
	ret = list(ret.items())
	ret.sort()
	return ret

def process2(X,S,R,t,accum):
	byspd = process3(X,S,accum)
	R -= S
	del X,S,accum
	ret = 0
	for spd,dist in byspd:
		maxdist = (spd+R)*t
		if dist < maxdist:
			tt = dist/(spd+R)
			t -= tt
		else:
			tt = t + (dist-maxdist)/spd
			t = 0
		ret += tt
	return ret

def process(f_, out = None):
	T_, = map(int,f_.readline().strip().split())
	for X_ in range(1,T_+1):
		X,S,R,t,N = map(int,f_.readline().strip().split())
		accum = []	
		for i_ in xrange(N):
			B,E,w = map(int,f_.readline().strip().split())
			accum.append((B,E,w))
		assert len(accum) == N
		output = process2(X,S,R,t,accum)
		
		out.write('Case #%d: %s\n' % (X_,output))
		out.flush()

TEST_DATA=(r'''
3
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1
	Case #1: 4.000000
Case #2: 5.500000
Case #3: 3.538095238
''',
#r'''  '''
)

# Running
def assertdebug(func):
	try:
		assert False
		return func
	except AssertionError:
		pass
	def pmfunc(*args,**kwargs):
		try:
			return func(*args,**kwargs)
		except:
			traceback.print_exc()
			pdb.post_mortem()
			raise
	return pmfunc
process=assertdebug(process)

def process_test(d):
	f_ = io.StringIO(d)
	out = io.StringIO()

	process(f_,out)

	ret = out.getvalue()
	return ret

def process_file(fn,auto=False):
	if fn.endswith('.in'):
		base = fn[:-3]
	elif fn.endswith('.in.txt'):
		base = fn[:-7]
	else:
		base = fn

	i = 0
	while True:
		path = '%s.out%d.txt'%(base,i)
		if not os.path.exists(path):
			break
		if auto:
			print "! %s exists"%path
			return
		i += 1
	print ">> %s"%path
	f_ = open(fn,'rb')
	out = open(path,'wb')

	process(f_,out)

	f_.close()
	out.close()

def main():
	def td(d):
		if isinstance(d,str):
			d=d.split('Case #1:',1)
			return d[0].strip(), 'Case #1:' + d[1].rstrip() + '\n'
		return d
	
	def ts(prefix='>',old=[None]):
		t = time.time()
		diff = (old[0] is not None) and ' d%.6f'%(t - old[0]) or ''
		old[0] = t
		print '%s %s %.6f%s'%(prefix,time.strftime('%F %T %z',time.gmtime(t)),t,diff)

	l = sys.argv[1:]
	auto=False
	if not l:
		ts('t')
		for test_data in TEST_DATA:
			if not test_data.strip():
				return
			test_input,expected_output=td(test_data)
			my_output = process_test(test_input)
			if my_output != expected_output:
				print >>sys.stderr, "!!! Wrong output."
				print >>sys.stderr, my_output
				return
			ts('v')
		mydir,myfile = os.path.split(os.path.join(os.path.curdir,__file__))
		assert os.path.abspath(mydir) == os.path.abspath(os.path.curdir)
		if myfile.endswith('.py') and len(myfile) == 4:
			expr = re.compile(r'\A%s\-(?:large|small-attempt[0-9]|(?:large|small)\-practice)\.in(?:\.txt)?\Z'%myfile[0].upper())
			auto=True
			for f in os.listdir(mydir):
				if expr.match(f):
					l.append(f)
	for x in l:
		ts('@')
		print '>> %s'%x
		process_file(x,auto=auto)
	ts('=')

if __name__ == '__main__':
	main()