#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
def check(v, w):
    assert w.count(1) == 720 and w.count(2) == 720
    for i in xrange(1440):
        if v[i] == 0:
            continue
        if v[i] != w[i]:
            return False
    return True


def ok2(v):
    w = [1] * 720 + [2] * 720
    if check(v, w):
        return True
    w = [2] * 720 + [1] * 720
    if check(v, w):
        return True
    return False


def ok3(v):
    for st in xrange(1, 720):
        ed = st + 720
        w = [1] * 1440
        for x in xrange(st, ed):
            w[x] = 2
        if check(v, w):
            return True
        w = [2] * 1440
        for x in xrange(st, ed):
            w[x] = 1
        if check(v, w):
            return True
    return False



def f(a, b, A, B):
    v = [0] * 1440
    for i in xrange(a):
        p, q = A[i]
        for x in xrange(p, q):
            v[x] = 2
    for i in xrange(b):
        p, q = B[i]
        for x in xrange(p, q):
            v[x] = 1
    if ok2(v):
        return 2
    if ok3(v):
        return 2
    return 4




T = int(raw_input())
for loop in xrange(T):
    a, b = map(int, raw_input().split())
    A = [None] * a
    B = [None] * b
    for i in xrange(a):
        A[i] = map(int, raw_input().split())
    for i in xrange(b):
        B[i] = map(int, raw_input().split())
    res = f(a, b, A, B)
    print 'Case #{}: {}'.format(loop+1, res)
