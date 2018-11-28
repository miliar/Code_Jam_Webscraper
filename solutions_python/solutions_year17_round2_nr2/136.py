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

good = set("GR RG RY YR YV VY RB BR YB BY BO OB".split())
# goodx = set("BR RB RY YR BY YB   BO OY OR OO   RG GY GB VV   YV VR VB GG".split())

def check(c, n, O, B):
    if c[O] == 0:
        return c
    if c[B] < c[O] or (c[B] == c[O] and c[B] + c[O] != n):
        raise RuntimeError()
    # c[B] -= c[O]
    return c

def solve(n, c):
    b, o = "BO"
    ps = ["BO", "YV", "RG"]
    mxes = []
    for b, o in ps:
        # epr(b, o, c[b], c[o])
        if c[b] == c[o] and c[b] + c[o] == n: return (b+o) * (n/2)
        if c[o] and c[b] <= c[o]: return "IMPOSSIBLE"
        if c[o]:
            mxes.append(range(1, c[b] - c[o] + 1))
        else:
            mxes.append((0,))
    # print mxes
    for ms in product(*mxes):
        cur = c.copy()
        for m, (b, o) in zip(ms, ps):
            cur[o] = 0
            cur[b] -= c[o]
            # cur[b] += m
        res = subsolve(sum(cur.values()), cur)
        # print cur, res
        if res == "IMPOSSIBLE":
            continue

        res = list(res)
        for m, (b, o) in zip(ms, ps):
            tabs = [b + o + b for _ in xrange(m)]
            if m:
                tabs[0] += (o + b) * (c[o] - m)
            for i in xrange(len(res)):
                if res[i] == b and tabs:
                    res[i] = tabs.pop()
            # print res
        res = "".join(res)
        return res
    return "IMPOSSIBLE"

def subsolve(n, c):
    # try:
    #     c = check(c, n, "O", "B")
    #     c = check(c, n, "G", "R")
    #     c = check(c, n, "V", "Y")
    # except RuntimeError:
    #     return "IMPOSSIBLE"
    # assert c["O"] == c["G"] == c["V"] == 0
    c = c.copy()
    res = []
    while max(c.values()) > 0:
        for k in list(c.keys()):
            if c[k] == 0:
                del c[k]
        # epr(res, c)
        for col, cnt in sorted(c.items(), key = lambda kv: (kv[1], kv[0] == (res and res[0])), reverse=True):
            if not cnt:
                continue
            # if res:
                # print "  ", col, cnt, res[-1] + col, (res[-1] + col) in goodx
            if not res or (res[-1] + col) in good:
                res += col
                c[col] -= 1
                break
        else:
            return "IMPOSSIBLE"
    # for i in xrange(len(res)):
    #     if res[i] == "O": res[i] = "OB"
    #     if res[i] == "G": res[i] = "GR"
    #     if res[i] == "V": res[i] = "VY"

    res = "".join(res)
    if (res[0]+res[-1]) not in good:
        return "IMPOSSIBLE"
    return res


cache = {}

def brute(n, prefix, c):
    if n == 0:
        if (prefix[-1] + prefix[0]) in good:
            return prefix
        return
    if prefix not in cache:
        for col, cnt in c.items():
            if (not prefix or (prefix[-1] + col) in good) and cnt > 0:
                c2 = c.copy()
                c2[col] -= 1
                res = brute(n - 1, prefix + col, c2)
                if res:
                    return res
        cache[prefix] = None


    # if O:
    #     if B < O + 1: return "IMPOSSIBLE"
    #     res += "BO" * O + "B"
    #     O = 0
    #     B -= O + 1
    #     B += 1
    # if G:
    #     if R < G + 1: return "IMPOSSIBLE"
    #     res += "RG" * G + "R"
    #     G = 0
    #     R -= G + 1
    #     R += 1
    # if V:
    #     if Y < V + 1: return "IMPOSSIBLE"
    #     res += "YV" * V + "V"
    #     V = 0
    #     Y -= V + 1
    #     Y += 1

# print solve(7, {'B': 2, 'G': 0, 'O': 0, 'R': 3, 'V': 0, 'Y': 2})
# print solve(7, {'B': 2, 'G': 0, 'O': 0, 'R': 3, 'V': 0, 'Y': 2})
# quit()
# print solve(5, {'B': 2, 'G': 0, 'O': 1, 'R': 1, 'V': 0, 'Y': 1})
# quit()
# t = 1000000
t = read_int()
for j in xrange(t):
    arr = read_ints()
    # arr = [0] * 6
    # for i in xrange(0, 6):
        # arr[i] = random.randint(0, 4)
    # arr = [None] + arr
    cs = dict(zip("ROYGBV", arr[1:]))
    n = sum(cs.values())

    assert n >= 3
    ans = solve(n, cs.copy())
    if 1 or n > 50:
        print "Case #%d: %s" % (j+1, ans)
        continue

    # print n
    cache.clear()
    ans2 = brute(n, "", cs.copy())
    # print ans, ans2
    if (ans == "IMPOSSIBLE") != (ans2 is None):
        print "WHAT", n, cs
        print ans
        print ans2
        quit()
    print "Case #%d: %s" % (j+1, ans)
    # epr()
