#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright © 2009-2012 by T. Chan.

from __future__ import division,with_statement
#from __future__ import absolute_import,print_function
import __builtin__,sys,os,os.path,re,time,hashlib,base64,StringIO as io,cPickle as pickle
import operator,array,itertools,bisect,collections
import pprint,pdb,traceback,warnings
from pdb import set_trace as debug
from math import hypot,pi,sin,cos,tan,sqrt,floor,ceil,asin,fsum
from itertools import islice,izip,imap
from collections import namedtuple,deque
from heapq import heappush,heappop

class Node(object):
	__slots__ = ('i','p','v')
	def __init__(self,p,v):
		self.i = None
		self.p = p
		self.v = v
	def __lt__(self,other):
		return self.p < other.p
	def __cmp__(self,other):
		return cmp(self.p,other.p)
	def __repr__(self):
		return 'Node(%r,%r,%r)'%(self.i,self.p,self.v)

# A priority-queue implementation based on the heapq module.
# The idea:
#   Override __setitem__ to store the heap index of a node n into n.i.
#   Add a method "heapfixdown(node)" that calls _siftdown() on the node's index. Call this if a node's decreases.
#   Force heapq to use the pure-Python implementation so overriding __setitem__ works.
class PrioQ(list):
	# Use heapq's Python implementation before "try: import _heapq". Works in Python 2.6.1 to 2.7.3rc2
	heapq = type(__builtin__)(name='heapq2')
	exec open((lambda x:x if x[-3:]=='.py' else x[:-1])(__import__('heapq').__file__),'rb').read().split('try:',1)[0] in heapq.__dict__
	def heapify(self,heapq=heapq):
		return heapq.heapify(self);
	def heappush(self,v,heapq=heapq):
		assert v.i is None
		return heapq.heappush(self,v)
	def heappop(self,heapq=heapq):
		v = heapq.heappop(self)
		v.i = None
		return v
	def heapfixdown(self,node,heapq=heapq):
		return heapq._siftdown(self,0,node.i)
	def __init__(self,*args):
		list.__init__(self,*args)
		self.heapify()
	def __setitem__(self,i,v):
		list.__setitem__(self,i,v)
		v.i = i
	def __setslice__(self,i,j,v):
		list.__setslice__(self,i,j,v)
		for x in xrange(i,j):
			self[x].i = x

def process2(levels):
	star1 = []
	star2 = []
	for s1,s2 in levels:
		complete = [s1,s2,0]
		star1.append(complete)
		star2.append(complete)
	star1.sort(key=lambda l:-l[0])
	star2.sort(key=lambda l:-l[1])
	star1ready = []
	ret = nstars = 0
	while star2:
		while star2 and star2[-1][2] >= 2:
			star2.pop()
		if not star2:
			break
		if nstars >= star2[-1][1]:
			c = star2.pop()
			assert c[2] in (0,1)
			nstars += 2-c[2]
			c[2] = 2
			ret += 1
			continue
		while star1:
			if star1[-1][2] >= 1:
				star1.pop()
				continue
			if nstars >= star1[-1][0]:
				c = star1.pop()
				assert c[2] == 0
				heappush(star1ready,(-c[1],c))
				continue
			break
		if star1ready and nstars >= star1ready[0][1][0]:
			c = heappop(star1ready)[1]
			if c[2] >= 1:
				continue
			assert c[2] == 0
			nstars += 1
			c[2] = 1
			ret += 1
			continue
		return 'Too Bad'
	return ret

def process(f_, out):
	T_, = map(int,f_.readline().strip().split())
	for X_ in range(1,T_+1):
		n_, = map(int,f_.readline().strip().split())
		accum=[]
		for i_ in xrange(n_):
			input = map(int,f_.readline().strip().split())
			assert len(input) == 2
			accum.append(input)
		output = process2(accum)
		
		out.write('Case #%d: %s\n' % (X_,output))
		out.flush()

TEST_DATA=(r'''
4
2
0 1
0 2
3
2 2
0 0
4 4
1
1 1
5
0 5
0 1
1 1
4 7
5 6

Case #1: 3
Case #2: 3
Case #3: Too Bad
Case #4: 6
''',)

# Running
def assertdebug(func):
	try: assert False; return func
	except AssertionError: pass
	def pmfunc(*args,**kwargs):
		try: return func(*args,**kwargs)
		except: traceback.print_exc(); pdb.post_mortem(); raise
	return pmfunc
process=assertdebug(process)

def process_test(d):
	f_,out = io.StringIO(d),io.StringIO()
	process(f_,out)
	return out.getvalue()

def process_file(fn,auto=False):
	for ext in ('.in', '.in.txt', ''):
		if fn.endswith(ext): base = fn[:-len(ext)] if ext else fn; break
	i = 0
	while 1:
		path = '%s.out%d.txt'%(base,i); path2 = 'broken-'+path
		p1,p2 = os.path.exists(path), os.path.exists(path2)
		if not (p1 or p2): break
		if auto and p1: print "! %s exists"%(path if p1 else path2); return
		i += 1
	print ">> %s"%path
	success = None
	try:
		with open(fn,'rb') as f_,open(path,'wb') as out: process(f_,out)
		success = True
	finally:
		if not success: os.rename(path,path2)
	return success

def main():
	def ts(prefix='>',delta=True,old=[None]):
		t = time.time()
		diff, old[0] = (delta and (old[0] is not None)) and ' d%.6f'%(t - old[0]) or '', t
		print '%s %s %.6f%s'%(prefix,time.strftime('%F %T %z',time.gmtime(t)),t,diff)

	ts(' ',delta=False)

	qid = rundir = testcache = None
	mydir,myfile = os.path.split(os.path.join(os.path.curdir,__file__))
	assert os.path.abspath(mydir) == os.path.abspath(os.path.curdir)
	if myfile.endswith('.py') and len(myfile) == 4:
		qid,rundir,t,myhash = myfile[0].upper(), os.path.join(mydir,'runs'), time.time(), hashlib.sha256()
		if not os.path.isdir(rundir): os.makedirs(rundir)
		runfile = os.path.join(rundir, '%s_%s.%06dz.py'%(qid,time.strftime('%F-%H%M%S',time.gmtime(t)),round(t%1*1e6)))
		assert not os.path.exists(runfile)
		with open(__file__,'rb') as fin, open(runfile,'wb') as fout:
			d = fin.readline()+fin.readline(); fout.write(d); myhash.update(d)
			fout.write('\n# RUN at %s %.6f\n# cmdline = %r\n\n'%(time.strftime('%F %T %z',time.gmtime(t)),t,sys.argv))
			d = fin.read(); fout.write(d); myhash.update(d)
		testcache = os.path.join(rundir,'%s_%s.passed'%(qid,base64.b32encode(myhash.digest()).rstrip('=')))
		del fin, fout, t, runfile, myhash

	if 'gen' in globals(): gen(os.path.join(mydir,myfile+'.pickle'), ts)
	l = sys.argv[1:]
	auto=False
	if not l:
		if not (testcache and os.path.exists(testcache)):
			def td(d):
				if isinstance(d,str): d=d.split('Case #1:',1); return d[0].strip(), 'Case #1:' + d[1].rstrip() + '\n'
				return d
			for test_data in TEST_DATA:
				if not test_data.strip(): print >>sys.stderr, '! Empty test case.'; return
				test_input,expected_output=td(test_data)
				my_output = process_test(test_input)
				if my_output != expected_output: print >>sys.stderr, "!!! Wrong output."; print >>sys.stderr, my_output; return
				ts('v')
			if testcache: open(testcache,'wb').close()
		if qid:
			expr = re.compile(r'\A%s\-(?:large|small-attempt[0-9]|(?:large|small)\-practice)\.in(?:\.txt)?\Z'%qid)
			auto=True
			l = list(f for f in os.listdir(mydir) if expr.match(f))
	for x in l:
		ts('.',delta=False)
		print '<< %s'%x
		if x == '-': process(sys.stdin,sys.stdout)
		else: process_file(x,auto=auto)
		ts('>')

if __name__ == '__main__':
	main()
