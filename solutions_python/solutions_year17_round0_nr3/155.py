# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Qualification Round
"""

from functools import lru_cache
from itertools import chain
import sys

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

@lru_cache(maxsize=None)
def calc(n) :
    assert n > 0
    if n == 1 :
        return {1: 1}
    elif n == 2 :
        return {1: 1, 2: 1}
    ma, mi = split(n)
    d = calc(ma)
    e = calc(mi)
    res = {n : 1}
    for k, v in chain(d.items(), e.items()) :
        res[k] = res.get(k, 0) + v
    return res
    
def split(n) :
    n -= 1
    return (n // 2 + n % 2), (n // 2)

def once():
    '''to cope once
    return the answer to be printed'''
    n, k = IO.gets(int)
    d = calc(n)
    cnt = 0
    for key, v in sorted(d.items(), reverse=True) :
        cnt += v
        if cnt >= k :
            return split(key)

def show(ans) :
    return "%d %d"%ans #IO.tostr(ans, writer=str, delim=' ')
    
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
