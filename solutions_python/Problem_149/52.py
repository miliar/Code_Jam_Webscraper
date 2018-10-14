
# coding: cp932

lines = iter('''
2
3
1 2 3
5
1 8 10 3 7
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

infile = 'B-small-attempt2.in'
infile = 'B-large.in'
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

def count(L):
	#X = sorted(L)
	cnt = 0
	while L:
		I = list(ir(len(L)))
		x = min(I, key=lambda n:L[n])
		cnt += x
		L = L[:x] + L[x+1:]
		#print(L)
		
	return cnt
		
		
#print(count([3,1,2,0]))
#exit()
def solve(N,A):
	if case == 12: import pdb;pdb.set_trace()
	X = list(ir(N))
	#X.sort(key=lambda n:A[n], reverse=True)
	#print(X, [A[x] for x in X])
	#count(X)
	x = max(X, key=lambda n:A[n])
	print(A)
	#print(x, A[x])
	#for i in 
	#count(A[:x]) + count(A[x+1][::-1])
	
	X = A[x]
	mid = N // 2
	cnt = abs(x-mid)
	#A = A[:x] + A[x+1:]
	#left  = A[:len(A)//2]
	#right = A[len(A)//2:][::-1]
	
	ans = MAX
	for i in ir(N):
		cnt = abs(x-i)
		if i == x:
			left = A[:i]
			right= A[i+1:][::-1]
		elif i< x:
			a = A[:x] + A[x+1:]
			left = a[:i]
			right= a[i:][::-1]
		else: # i > x
			a = A[:x] + A[x+1:]
			left = a[:i-1]
			right= a[i-1:][::-1]
		t = count(left) + cnt + count(right)
		#print(t, i, right, left)
		ans = min(ans, t)
	#print(ans)
	return ans
			
	A = A[:x] + A[x+1:]
	left  = A[:len(A)//2]
	right = A[len(A)//2:][::-1]
	
	
	return count(left) + cnt + count(right)
	#A = A[:x] + A[x+1:]
	#N = len(A)
	mn = MAX
	for n in range(1<<N):
		a = deepcopy(A)
		for j in range(N):
			if (n>>j)&1:
				a[j] = X*10-a[j]
		mn = min(count(a), mn)
	return mn
	
def solve(N,A):
	ans = 0
	#if case == 12: import pdb;pdb.set_trace()
	while A:
		N = len(A)
		L = list(ir(N))
		x = min(L, key= lambda n:A[n])
		if x == 0 or x == N-1:
			A = A[:x]+ A[x+1:]
			continue
			
		a = min(N - x - 1, x)
		ans += a
		A = A[:x]+ A[x+1:]
	return ans

#dll = cdll.LoadLibrary(r'x64\Release\c.dll')
#dll.solve.restype = c_int
#dll.solve.argtypes= (c_int,c_int,c_int,CFUNCTYPE(None, c_void_p))

caseCnt = int(next(lines))
for case in range(1, caseCnt+1):
	(N,) = map(int, next(lines).split())
	(*A,) = map(int, next(lines).split())
	start = time.time()
	print('Case #%d:'%(case), solve(N,A), file=out)
	print(time.time()-start)

