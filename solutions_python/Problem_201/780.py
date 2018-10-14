#!/usr/bin/python

from heapq import *
from bt    import *

def pop()       : k, cnt = del_max(); return k, cnt
def push(k, cnt): ins(k, cnt)

def ir():                          return int(raw_input())
def ia(): l = raw_input().split(); return map(int, l)

def intwo(A):
    if A % 2 == 0: return A//2, A//2
    else         : return A//2, A//2 + 1

def solve():
    n, K = ia()
    reset(); push(n, cnt=1)
    while True:
        if K <= 0: break
        b, cnt = pop(); K -= cnt
        p1, p2 = intwo(b - 1)
        push(p1, cnt); push(p2, cnt)
    return p1, p2
    
for it in xrange(1, ir()+1):
    ans = solve()
    print "Case #%d:" % it, ans[1], ans[0]
