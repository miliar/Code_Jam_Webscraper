
# coding: cp932

lines = iter('''
3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60
'''.splitlines(False)[1:])


from math import sqrt
from datetime import datetime
import sys
class Out:
	def __init__(me, f):
		me.file = f
	def write(me, *args):
		sys.stdout.write(*args)
		me.file.write(*args)
out = sys.stdout
#sys.setrecursionlimit(1500)

#from decimal import Decimal, getcontext
#getcontext().prec = 64

date = datetime.now().strftime('%Y%m%d-%H%M%S')

infile = 'A-small-attempt0.in'
infile = 'A-large.in'
lines = iter(open(infile).read().splitlines(False))
out = Out(open(infile[:-3] + (date + '.answer'), 'w'))

import time
from collections import namedtuple, defaultdict
from itertools import count, product, combinations
from ctypes import*

from copy import deepcopy

MAX = float('inf')

import sys
sys.setrecursionlimit(1500)

from math import log, cos, sin
import time
import inspect

#print(setup(3, 4))

MIN = -float('inf')
MAX = float('inf')

def gdc(P,Q):
	r = P%Q
	if r == 0:
		return Q
	return gdc(Q,r)
	
	
		

#T = Union(100)
#print(T.top(1))
#print(T.tail(1))
#T.combine(1,0)
#print(T.top(1))
#print(T.tail(1))

ie = enumerate
ir = range
ic = combinations
ip = product


def solve(N,X,F):
	F.sort(reverse=True)
	#print(N,X,F)
	cnt = 0
	while F:
		cnt += 1
		f = F.pop()
		if f > X: raise
		for i,t in ie(F):
			if f+t <= X:
				F = F[:i] + F[i+1:]
				break
	return cnt
#dll = cdll.LoadLibrary(r'x64\Release\c.dll')
#dll.solve.restype = c_int
#dll.solve.argtypes= (c_int,c_int,c_int,CFUNCTYPE(None, c_void_p))

caseCnt = int(next(lines))
for case in range(1, caseCnt+1):
	(N,X) = map(int, next(lines).split())
	(*F,) = map(int, next(lines).split())
	start = time.time()
	print('Case #%d:'%(case), solve(N,X,F), file=out)
	print(time.time()-start)

