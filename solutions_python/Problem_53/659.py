#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

ANS = {True:'ON', False:'OFF'}

def get_mod_k(N, K):
    return K % (2 ** N)

def is_on(N, K):
    return (2 ** N) == (K + 1) 

def get_state(N, K):
    K = get_mod_k(N, K)
    return is_on(N, K) 

if __name__ == '__main__':
    T = readint()
    for t in xrange(1, T+1):
        N, K = readlinearray(int)
        state = get_state(N, K)
        print 'Case #%d: %s' % (t, ANS[state])
