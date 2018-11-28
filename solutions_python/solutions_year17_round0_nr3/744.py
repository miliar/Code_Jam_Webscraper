#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, math, random, operator
from string import ascii_lowercase, ascii_uppercase
from fractions import Fraction, gcd
#from decimal import Decimal, getcontext
from itertools import product, permutations, combinations
from Queue import Queue, PriorityQueue
from collections import deque, defaultdict, Counter
#getcontext().prec = 100

MOD = 10**9 + 7
INF = float("+inf")

if sys.subversion[0] == "PyPy":
    import io, atexit
    sys.stdout = io.BytesIO()
    atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
    sys.stdin = io.BytesIO(sys.stdin.read())
    raw_input = lambda: sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
die = lambda *args: pr(*args) ^ exit(0)

read_str = raw_input
read_strs = lambda: raw_input().split()
read_int = lambda: int(raw_input())
read_ints = lambda: map(int, raw_input().split())
read_float = lambda: float(raw_input())
read_floats = lambda: map(float, raw_input().split())

"---------------------------------------------------------------"

def solve(n, k):
    count = defaultdict(int)
    pq = PriorityQueue()
    pq.put(-n)
    count[n] = 1
    while k > 0:
        v = -pq.get()
        cnt = count[v]
        # print i, v, cnt
        del count[v]
        if v == 0:
            return 0, 0
        v -= 1
        a = v / 2
        b = v - a
        if count[a] == 0:
            pq.put(-a)
        if count[b] == 0 and b != a:
            pq.put(-b)
        count[a] += cnt
        count[b] += cnt
        k -= cnt
    return max(a, b), min(a, b)




t = read_int()
for i in xrange(t):
    n, k = read_ints()
    ans = solve(n, k)
    print "Case #%d: %s %s" % (i+1, ans[0], ans[1])
