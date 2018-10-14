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

def process3(R,C,board):
	board = list(list(r) for r in board)
	cumul = [((0,0,0),)*(C+1)] + list([(0,0,0)]+[None]*C for i in xrange(R))
	for y in xrange(R):
		for x in xrange(C):
			assert cumul[y+1][x+1] is None
			m = board[y][x]
			mx,my = m*x,m*y
			board[y][x] = (m,mx,my)
			upm,upmx,upmy = cumul[y][x+1]
			ltm,ltmx,ltmy = cumul[y+1][x]
			ulm,ulmx,ulmy = cumul[y][x]
			c_m = m + upm + ltm - ulm
			c_mx = mx + upmx + ltmx - ulmx
			c_my = my + upmy + ltmy - ulmy
			cumul[y+1][x+1] = c_m,c_mx,c_my
	return board,cumul


def process2(R,C,board):
	board,cumul = process3(R,C,board)
	def getv(x0,y0,x1,y1):
		c_m,c_mx,c_my = cumul[y1][x1]
		upm,upmx,upmy = cumul[y0][x1]
		ltm,ltmx,ltmy = cumul[y1][x0]
		ulm,ulmx,ulmy = cumul[y0][x0]
		tlm,tlmx,tlmy = board[y0][x0]
		trm,trmx,trmy = board[y0][x1-1]
		blm,blmx,blmy = board[y1-1][x0]
		brm,brmx,brmy = board[y1-1][x1-1]
		m = c_m - upm - ltm + ulm - tlm - trm - blm - brm
		mx = c_mx - upmx - ltmx + ulmx - tlmx - trmx - blmx - brmx
		my = c_my - upmy - ltmy + ulmy - tlmy - trmy - blmy - brmy
		return m,mx,my
	best = 0
	for y in xrange(R+1):
		for x in xrange(C+1):
			for size in xrange(3,min(R+1-y,C+1-x)):
				#if x == 1 and y == 1 and size == 5:
				#	debug()
				assert size <= min(R,C)
				m,mx,my = getv(x,y,x+size,y+size)
				# we want  mx/m == x+size/2  and  my/m == y+size/2
				# 2*mx == (2*x+size)*m
				if 2*mx == (2*x+size-1)*m and 2*my == (2*y+size-1)*m:
					best = max(best,size)
	if not best:
		return 'IMPOSSIBLE'
	return best

def process(f_, out = None):
	T_, = map(int,f_.readline().strip().split())
	for X_ in range(1,T_+1):
		R,C,D = map(int,f_.readline().strip().split())

		accum = []	
		for i_ in xrange(R):
			input = tuple(map(int,f_.readline().strip()))
			assert len(input) == C
			accum.append(input)
		assert len(accum) == R

		output = process2(R,C,accum)
		#output = '%d'%output
		#output = '%.6f'%output
		
		out.write('Case #%d: %s\n' % (X_,output))
		out.flush()

TEST_DATA=(r'''
2
6 7 2
1111111
1122271
1211521
1329131
1242121
1122211
3 3 7
123
234
345
	Case #1: 5
Case #2: IMPOSSIBLE

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