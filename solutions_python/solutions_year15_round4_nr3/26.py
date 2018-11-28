#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

rl = sys.stdin.readline
def rs():
    return rl().split()

def ri():
    return int(rl())

def rvi():
    return map(int, rs())

def identer(d, s):
    if s in d:
        return d[s]
    else:
        r = len(d)
        d[s] = r
        return r

def main():
    T = ri()
    for tc in xrange(1, T+1):
        N = ri()
        a = []
        d = {}
        for i in xrange(N):
            v = []
            for s in rs():
                v.append(identer(d, s))
            a.append(list(set(v)))
        keng = set(a[0])
        kfr = set(a[1])
        eng = set()
        fr = set()
        for x in a[2:]:
            for y in x:
                if y in keng:
                    keng.remove(y)
                    eng.add(y)
                if y in kfr:
                    kfr.remove(y)
                    fr.add(y)
        a = a[2:]
        N -= 2
        best = 1000000000
        for i in xrange(1 << N):
            te = eng.copy()
            tf = fr.copy()
            t = i
            for j in xrange(N):
                if t & 1:
                    te.update(a[j])
                else:
                    tf.update(a[j])
                t >>= 1
            best = min(best, len(te.intersection(tf)))
        print "Case #%d: %d" % (tc, best + len(kfr.intersection(keng)))



if __name__ == '__main__':
    main()
