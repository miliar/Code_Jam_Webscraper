#!/usr/bin/env python

import sys

mem = {}
def f(s,t):
    # return the number of ways of spelling s from t
    if (s,t) in mem:
        return mem[(s,t)]
    if len(s) == 1:
        return t.count(s)
    c=s[0]
    tot = 0
    for i,C in enumerate(t):
        if c != C:
            continue
        tot += f(s[1:], t[i:])

    mem[(s,t)] = tot
    return tot%10000

s="""So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."""
assert f("welcome to code jam", s) == 3727

ff=sys.stdin
N = int(ff.next())
for i in range(1,N+1):
    t = ff.next().strip()
    
    print "Case #%s: %s"%(i,str(f("welcome to code jam",t)).zfill(4))
