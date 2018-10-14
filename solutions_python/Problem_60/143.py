#!/usr/bin/env python2.6
# -*- Mode: python; indent-tabs-mode: nil; py-indent-offset: 4; python-indent: 4; -*-
# vim:expandtab softtabstop=4 shiftwidth=4:
import sys

def Swaps(N, K, B, T, xs, vs):
    s = 0
    imps = 0
    for i in range(N-1, -1, -1):
        if K <= 0: break
        x = xs[i]; v = vs[i]
        if (B-x) > v*T:
            imps += 1
            continue
        #print K, i, s, imps
        s += imps
        K -= 1
    if K <= 0: return str(s)
    return 'IMPOSSIBLE'
def main():
    it = iter(sys.stdin)
    T = int(next(it))
    for i in range(T):
        N, K, B, T = map(int, next(it).split())
        x = map(int, next(it).split())
        v = map(int, next(it).split())
        assert len(x) == N
        assert len(v) == N
        print "Case #%d: %s" %(i+1, Swaps(N, K, B, T, x, v))

if __name__=="__main__":
    main()
