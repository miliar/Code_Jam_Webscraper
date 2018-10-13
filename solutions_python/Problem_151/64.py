
# coding: cp932

lines = iter('''
2
4 2
AAA
AAB
AB
B
5 2
A
B
C
D
E
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

infile = 'D-small-attempt0.in'
#infile = 'B-large-practice.in'
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

MOD = 1000000007

def solve(M,N,S):
	G = [[0]*M for i in ir(M)]
	for i,j in ic(ir(M), 2):
		s = S[i]
		s2= S[j]
		for n in ir(min(len(s), len(s2))):
			if s[n] != s2[n]:break
		else:
			n += 1
		G[i][j] = n
		G[j][i] = n
	for g in G:print(g)
	#print(M,N,S)
def solve(M,N,S):
	ans = 0
	cnt = 0
	used = set()
	for n in range(N**M):
		D = [0]*M
		for i in ir(M):
			D[i] = n%N
			n //= N

		#temp = ['']*N
		#for i,s in ie(S):
		#	temp[D[i]] += s
		#temp.sort()
		#temp = tuple(temp)
		#if temp in used:
		#	continue
		#used.add(temp)
		
		#temp = [0]*N
		#for i in ir(N):
		#	temp[D[i]] += 1
		#if 0 in temp: continue
		
		T = [set() for _ in ir(N)]
		for i,s in ie(S):
			t = T[D[i]]
			for j,_ in ie(s):
				t.add(s[:j+1])
		#print(T)
		c = sum([len(t)+1 if t else 0 for t in T])
		if ans < c:
			ans = c
			cnt = 1
		elif ans == c:
			cnt += 1
		#ans = max(c,ans)
	return '%d %d'%(ans, cnt)
	
#dll = cdll.LoadLibrary(r'x64\Release\c.dll')
#dll.solve.restype = c_int
#dll.solve.argtypes= (c_int,c_int,c_int,CFUNCTYPE(None, c_void_p))

caseCnt = int(next(lines))
for case in range(1, caseCnt+1):
	(M,N) = map(int, next(lines).split())
	S = []
	for _ in ir(M):
		(s,) = map(str, next(lines).split())
		S += [s]
	start = time.time()
	print('Case #%d:'%(case), solve(M,N,S), file=out)
	print(time.time()-start)

