#!/usr/local/bin/python2.7
#coding=UTF-8

# Copyright © 2009-2011 by T. Chan.

# Reading start: 2011-05-21 01:00:37 +0000 1305939637.987874
# Code start:    2011-05-21 01:29:15 +0000 1305941355.205353
# Test pass:     
# Small dl:      
# Small run:     
# Small accept:  
# Large dl:      
# Large run:     
# Large submit:  
# Complete:      

from __future__ import division
from StringIO import StringIO
import sys, os, re, os.path, time, operator,__builtin__,array
import pprint,pdb,traceback
from pdb import set_trace as debug
from math import hypot,pi,sin,cos,tan,sqrt,floor,ceil,asin

if not 'set' in __builtin__.__dict__:
	from sets import Set as set
	from sets import ImmutableSet as frozenset

def gcd(a,b):
	a,b = map(abs,(a,b))
	if a < b:
		a,b = b,a
	while b:
		a,b = b, a%b
	return a

def gcdivide(*args):
	if len(args) < 1:
		if not args:
			raise ValueError()
		a, = args
		if a == 0:
			return 0
		return a//abs(a)
	gcd_ = reduce(gcd,args)
	return list(x/gcd_ for x in args)

def process2(N,Pd,Pg):
	if Pg == 0 and Pd != 0:
		return False
	if Pg == 100 and Pd != 100:
		return False
	d,D = gcdivide(Pd,100)
	if not (D <= N):
		return False
	# d/D == Pd/100
	assert d*100 == Pd*D
	assert D > 0
	g = 200*Pg
	G = 200*100
	assert G >= D
	assert g >= d
	return True

def process(f_, out = None):
	T_, = map(int,f_.readline().strip().split())
	for X_ in range(1,T_+1):
		N,Pd,Pg = map(int,f_.readline().strip().split())

		output = process2(N,Pd,Pg)
		output = ('Broken','Possible')[output]
		
		out.write('Case #%d: %s\n' % (X_,output))
		out.flush()

TEST_DATA=('''
3
1 100 50
10 10 100
9 80 56
	Case #1: Possible
Case #2: Broken
Case #3: Possible

''')

def assertdebug(func):
	try:
		assert False
		return func
	except AssertionError:
		pass
	def pmfunc(*args,**kwargs):
		try:
			func(*args,**kwargs)
		except:
			traceback.print_exc()
			pdb.post_mortem()
	return pmfunc
process=assertdebug(process)

def process_test(d):
	f_ = StringIO(d)
	out = StringIO()

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
			d=d.split('Case #1: ',1)
			return d[0].strip(), 'Case #1: ' + d[1].rstrip() + '\n'
		return d
	
	def ts(prefix='>',old=[None]):
		t = time.time()
		diff=''
		if old[0] is not None:
			diff = ' d%.6f'%(t - old[0])
		old[0] = t
		print '%s %s %.6f%s'%(prefix,time.strftime('%F %T %z',time.gmtime(t)),t,diff)

	l = sys.argv[1:]
	ts('+')
	if not l:
		if not TEST_DATA.strip():
			return
		test_input,expected_output=td(TEST_DATA)
		my_output = process_test(test_input)
		if my_output != expected_output:
			print >>sys.stderr, "!!! Wrong output."
			print >>sys.stderr, my_output
			return
		mydir,myfile = os.path.split(__file__)
		assert os.path.abspath(mydir) == os.path.abspath(os.path.curdir)
		if myfile.endswith('.py') and len(myfile) == 4:
			expr = re.compile(r'\A%s\-(?:large|small-attempt[0-9]|(?:large|small)\-practice)\.in(?:\.txt)?\Z'%myfile[0].upper())
			for f in os.listdir(mydir):
				if expr.match(f):
					ts('@')
					print '>> %s'%f
					process_file(f,auto=True)
	for x in l:
		ts('@')
		print '>> %s'%x
		process_file(x)
	ts('=')

if __name__ == '__main__':
	main()