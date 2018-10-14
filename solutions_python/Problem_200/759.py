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

def solve(n):
    n = map(int, str(n))
    n0 = n[::]
    for i in xrange(len(n)):
        n2 = n[::]
        for d in reversed(range(10)):
            for j in xrange(i, len(n)):
                n2[j] = d
            if n2 <= n0:
                # print "GOOD", n2, n
                break
        n = n2
    return "".join(map(str, n)).lstrip("0")


t = read_int()
for i in xrange(t):
    m = read_int()
    ans = solve(m)
    ans = int(ans)
    if 0:
        ans_brute = solve(m)
        assert ans_brute == ans
    assert ans <= m, (ans, m)
    print "Case #%d: %s" % (i+1, ans)
