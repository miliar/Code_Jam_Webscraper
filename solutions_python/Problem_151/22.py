#!/usr/bin/python3

import sys
import itertools

class Trie(object):
    
    def __init__(self):
        self.children = {}
    
    def node_cnt(self):
        return 1 + sum(v.node_cnt() for v in self.children.values())
    
    def insert(self, niz):
        if niz == '':
            return
        if niz[0] not in self.children:
            self.children[niz[0]] = Trie()
        self.children[niz[0]].insert(niz[1:])    

def trie_cost(p, n, s):
    tries = [Trie() for i in range(n)]
    for niz, t in zip(s, p):
        tries[t-1].insert(niz)
    return sum([t.node_cnt() for t in tries])

def solve(n, m, s):
    cnt = 0
    cost = 0
    for p in itertools.product(range(1, n+1), repeat=m):
        if len(set(p)) < n:
            continue
        # print(p)
        tc = trie_cost(p, n, s)
        if tc > cost:
            cost = tc
            cnt = 1
        elif tc == cost:
            cnt += 1
    return cost, cnt

t = int(sys.stdin.readline())

for test_case in range(1, t+1):
    m, n = map(int, sys.stdin.readline().split())
    s = [sys.stdin.readline().strip() for i in range(m)]
    x, y = solve(n, m, s)
    y = y % 1000000007
    print('Case #%d: %d %d' % (test_case, x, y))
    