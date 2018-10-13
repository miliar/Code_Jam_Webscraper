# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1B
"""

import sys
from collections import Counter

class IO :
    def get(reader=str) :
        return reader(input().strip())
    def gets(reader=str, delim=None) :
        return [reader(x) for x in input().strip().split(delim)]
    def tostr(raw, writer=str, delim=' ') :
        return delim.join(writer(x) for x in raw)

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    pass


def once():
    n, c, m = IO.gets(int)
    pcs = [IO.gets(int) for _ in range(m)]
    dpc = Counter(p for p, c in pcs)
    dcp = Counter(c for p, c in pcs)
    for ans in range(max(dcp.values()), m+1) :
        n_empty = 0
        n_promo = 0
        for p in range(1, n+1) :
            if dpc[p] <= ans :
                n_empty += ans - dpc[p]
            else :
                n_promo += dpc[p] - ans
                n_empty -= n_promo
                if n_empty < 0 :
                    break
        if not n_empty < 0 :
            return ans, n_promo

def show(ans) :
    return IO.tostr(ans, writer=str, delim=' ')
    
def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = IO.get(int)
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, show(ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework done with", msg, file=sys.stderr)
    main()
