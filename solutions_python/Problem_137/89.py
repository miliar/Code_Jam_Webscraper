#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

memo = set()
ans = {}

def gen(r,c):
    global memo, ans

    assert r <= c

    memo = set()
    ans = {}

    if r == 1:
        sp = 1
        while sp <= c:
            ans[sp] = [sp]
            sp += 1
        return

    ans[1] = [1]*1 + [0]*(r-1)

    w = 2
    while w <= c:
        # 4,6,8,10,...,2c
        ans[w*2] = [w]*2 + [0]*(r-2)
        w += 1

    if r >= 3 and c >= 3:
        w = 3
        while w <= c:
            # 9,11,13,
            if (w*2+3) not in ans:
                ans[w*2+3] = [w]*2 + [3]*1 + [0]*(r-2-1)
            w += 1

    h = 2
    while h < r:
        w = 2
        while w <= c:
            if (c*h+w) not in ans:
                ans[c*h+w] = [c]*h + [w]*1 + [0]*(r-h-1)
            w += 1
        if h > 2 and (c*h+1) not in ans:
            ans[c*h+1] = [c]*(h-1) + [c-1]*1 + [2]*1 + [0]*(r-h-1)
        h += 1


def play(r,c):
    if r <= c:
        gen(r,c)
        return False
    else:
        gen(c,r)
        return True

def render(r,c,a,do_turn):
    m = []
    for j in range(r):
        m.append(['*'] * c)

    if do_turn:
        for j in range(c):
            for i in range(a[j]):
                m[i][j] = '.'
        pass
    else:
        for j in range(r):
            for i in range(a[j]):
                m[j][i] = '.'

    m[0][0] = 'c'
    for row in m:
        print ''.join(row)

def solve(r,c,m):
    # print "solve %dx%d + %d" % (r,c,m)
    do_turn = play(r,c)
    sp = r*c - m # スペース
    if sp in ans:
        render(r,c,ans[sp],do_turn)
    else:
        print "Impossible"


def main():
    t = input()
    for i in range(t):
        r,c,m = map(int, raw_input().split(' '))
        print "Case #%d:" % (1+i) #, (r,c,m)
        solve(r,c,m)

if __name__ == '__main__':
    main()

