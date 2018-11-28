#!/usr/bin/python2.5
import sys
sys.setrecursionlimit(100000)

mod = 1000000007
mem = {}

def solve(lst):
    if lst == []: return 0
    key = (lst[0], len(lst))
    if key in mem:
        return mem[key]

    n = 0
    for i in range(len(lst)):
        n += count_subseq(lst[i:], lst[i])

    mem[key] = n
    return n

def count_subseq(lst, val):
    key = (lst[0], len(lst), val)
    if (key) in mem:
        return mem[key]

    if (len(lst) == 1):
        return 1
    n = 1
    g = [x for x in lst if x > val]
    n += solve(g)
    mem[key] = n
    return n

for case in range(input()):
    n, m, X, Y, Z = [int(x) for x in raw_input().split()]
    mem = {}
    limits = []
    A = []
    for i in range(m):
        A.append(input())
    for i in range(n):
        limits.append(A[i % m])
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

    print "Case #%s: %s" % (case + 1, solve(limits) % mod )


