import sys
import re
import os
import time
from itertools import *
from pprint import pprint
from bisect import bisect

check = False

class FenwickTree(object):
	__slots__ = ["size", "sum"]

	def __init__(self, size):
		self.size = 1
		while self.size < size:
			self.size *= 2
		self.sum = [0 for i in range(self.size)]

	def update(self, i, delta):
		while i < self.size:
			self.sum[i] += delta
			i += self.F(i)

	def count(self, i):
		""" sum of elements in range(i) """
		res = 0
		i -= 1
		while i >= 0:
			res += self.sum[i]
			i -= self.F(i)
		return res

	@staticmethod
	def F(x):
		return x+1-((x+1)&x)

if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

def zero(n):
    return [(i,0) for i in range(n)]

def naiveOne(k, g):
    result = []
    for start in range(len(g)):
        q = g[start:]+g[:start]
        s = 0
        i = 0
        while i < len(q) and s+q[i] <= k:
            s += q[i]
            i += 1
        result.append(((start+i)%len(g),s))
    return result

def one(k, g):
    result = []
    f = FenwickTree(len(g))
    for i,x in enumerate(g):
        f.update(i, x)

    for start in range(len(g)):
        class SumArr(object):
            def __len__(self):
                return len(g)+1
            def __getitem__(self, i):
                if start+i <= len(g):
                    return f.count(start+i)-f.count(start)
                else:
                    return f.count(start+i-len(g))+f.count(len(g))-f.count(start)
        sumArr = SumArr()
        i = bisect(sumArr, k)-1
        result.append(((start+i)%len(g), sumArr[i]))

    if check:
        assert result == naiveOne(k, g)
    return result

def mul(v1, v2):
    assert len(v1) == len(v2)
    result = [None]*len(v1)
    for i, (j, s) in enumerate(v1):
        q, w = v2[j]
        result[i] = (q, w+s)
    return result

def naivePow(v, n):
    result = zero(len(v))
    for i in range(n):
        result = mul(result, v)
    return result

def pow(v, n):
    if n == 0:
        return zero(len(v))
    if n == 1:
        return v
    x = pow(mul(v,v),n//2)
    if n%2 == 1:
        x = mul(x,v)
    if check:
        assert x == naivePow(v,n)
    return x

def solve():
    R, k, N = map(int, next(fin).split())
    g = map(int, next(fin).split())
    assert len(g) == N

    x = one(k,g)

    print>>fout,pow(x,R)[0][1]

numCases = int(next(fin))
for caseNo in range(numCases):
    print '\b'*10,100*caseNo/numCases,'%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)