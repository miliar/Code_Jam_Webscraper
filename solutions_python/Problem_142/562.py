#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def remove_tuples(s):
    res = s[0]
    for k in xrange(1, len(s)):
        if res[-1] != s[k]:
            res += s[k]
    return res

def count_tuples(s):
    res = []
    c = 1
    for k in xrange(1, len(s)):
        if s[k-1] == s[k]:
            c += 1
        else:
            res.append(c)
            c = 1
    res.append(c)
    return res

def play(t, nb):
    s0 = remove_tuples(t[0])
    p = []
    m = [0] * len(s0)
    for s in t:
        p.append(count_tuples(s))
        if remove_tuples(s) != s0:
            return 'Fegla Won'
    for x in p:
        for k in xrange(len(m)):
            m[k] += x[k]
    for k in xrange(len(m)):
        m[k] = int(round(m[k]*1./nb))
    res = 0
    for x in p:
        for k in xrange(len(m)):
            res += abs(x[k] - m[k])
    return str(res)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        buf = f.read()
    t = buf.split("\n")
    nb_boards = int(t[0])
    t = t[1:]
    l = 0
    for k in xrange(0, nb_boards):
        nb = int(t[l])
        print "Case #%d: %s"%(k+1, play(t[l+1:l+1+nb], nb))
        l += nb + 1
