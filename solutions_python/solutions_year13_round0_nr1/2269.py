#!/usr/bin/python

import os, sys

periods = 0

def count(b, r, c, dr, dc):
    d = {'X': 0, 'O': 0, 'T': 0, '.': 0}
    for i in range(4):
        d[b[r][c]] += 1
        r += dr
        c += dc
    return d['X'], d['O'], d['T'], d['.']

# True if win
def check(x, o, t, p):
    global periods
    periods += p
    if x == 4 or x == 3 and t == 1:
        print 'X won'
        return True
    if o == 4 or o == 3 and t == 1:
        print 'O won'
        return True
    return False

T = int(raw_input())

for i in range(T):
    print 'Case #%d:' % (i+1),
    goon = False
    periods = 0
    b = []
    for j in range(4):
        a = ''
        while not a: a = raw_input()
        b.append(list(a))
    # rows
    r, c = 0, 0
    for i in range(4):
        if check(*count(b, r, c, 0, 1)):
            goon = True
            break
        r += 1
    if goon: continue
    # cols
    r, c = 0, 0
    for i in range(4):
        if check(*count(b, r, c, 1, 0)):
            goon = True
            break
        c += 1
    if goon: continue
    # diags
    if check(*count(b, 0, 0, 1, 1)): continue
    if check(*count(b, 0, 3, 1, -1)): continue
    # draw/end
    if periods == 0:
        print 'Draw'
    else:
        print 'Game has not completed'
    pass


