#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin, stdout

def compute_cost(queries, n):
    cost = 0
    for (o,e,p) in queries:
        x = e - o
        cost += p * (2*n-x) * (x + 1) / 2
    return cost

def fix_queries(queries):
    events = []
    for (o,e,p) in queries:
        events.append((o,-1,p))
        events.append((e,+1,p))
    fixed_queries = []
    p_stack = []
    for (s, t, p) in sorted(events):
        if t == -1:
            p_stack.append((s, p))
        else:
            while p != 0:
                while p_stack[-1][1] == 0:
                    p_stack.pop()
                so, sp = p_stack[-1]
                q = min(p, sp)
                fixed_queries.append((so, s, q))
                p -= q
                sp -= q
                p_stack[-1] = (so, sp)
    return fixed_queries

def solve():
    n,m = map(int, stdin.readline().strip().split())
    queries = []
    for i in range(m):
        o,e,p = map(int, stdin.readline().strip().split())
        queries.append((o,e,p))
    cost = compute_cost(queries, n)
    new_cost = compute_cost(fix_queries(queries), n)
    return cost - new_cost

if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        print("Case #{0}: {1}".format(i+1, solve()))
