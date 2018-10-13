#!/usr/bin/env python2.6
# -*- Mode: python; indent-tabs-mode: nil; py-indent-offset: 4; python-indent: 4; -*-
# vim:expandtab softtabstop=4 shiftwidth=4:
import sys

def Fill(tree, p, start=1):
    if start >= len(p): return 0
    name = p[start]
    if name in tree:
        return Fill(tree[name], p, start+1)
    st = dict()
    tree[name] = st
    return 1 + Fill(st, p, start+1)
def NumMkdir(e, n):
    #print e, n
    tree = dict()
    for p in e:
        Fill(tree, p.split('/'))
    r = 0
    for p in n:
        r += Fill(tree, p.split('/'))
    return r

def main():
    it = iter(sys.stdin)
    T = int(next(it))
    for t in range(T):
        N, M = map(int, next(it).split())
        e = list()
        for i in range(N):
            e.append(next(it).strip())
        n = list()
        for i in range(M):
            n.append(next(it).strip())
        print "Case #%d: %s" %(t+1, NumMkdir(e, n))

if __name__=="__main__":
    main()
