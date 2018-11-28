# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1B
"""

from itertools import product
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

def once():
    '''to cope once'''
    n, q = IO.gets(int)
    es, ss = zip(*[IO.gets(int) for _ in range(n)])
    d = [IO.gets(int) for _ in range(n)]
    us, vs = zip(*[IO.gets(int) for _ in range(q)])
    
    d = [[x if x != -1 else float('inf') for x in r] for r in d]
    
    for k, i, j in product(range(n), repeat=3) :
        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
    for i, j in product(range(n), repeat=2) :
        d[i][j] = d[i][j] / ss[i] if d[i][j] <= es[i] else float('inf')
        
    for k, i, j in product(range(n), repeat=3) :
        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    
    return [d[u-1][v-1] for u, v in zip(us, vs)]

def show(ans) :
    return IO.tostr(ans) #IO.tostr(ans, writer=str, delim=' ')
    
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
