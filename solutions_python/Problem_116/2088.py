#!/usr/bin/env python
# encoding: utf-8

def test(m):
    tran = {'X':-1,'T':0,'O':1,'.':100}
    rsum = [ sum([ tran[i] for i in r]) for r in m ]
    cols = [ [ r[i] for r in m ] for i in range(4) ]
    csum = [ sum([ tran[i] for i in c]) for c in cols]
    dsum = [ sum([ tran[m[i][i]] for i in range(4) ]),
             sum([ tran[m[i][3-i]] for i in range(4) ]) ]

    for s in rsum+csum+dsum:
        if s <= -3:
            return 'X won'
        elif 3 <= s <= 4:
            return 'O won'
    if sum(rsum+csum) > 50:
        return 'Game has not completed'
    else:
        return 'Draw'

def do_input():
    n = raw_input()
    a = []
    try:
        n = int(n)
    except:
        return
    else:
        for i in range(n):
            tmp = []
            tmp = [raw_input() for i in range(4)]
            raw_input()
            a.append(tmp)
        for idx,m in enumerate(a):
            print 'Case #{0}: '.format(idx+1)+test(m)

do_input()
