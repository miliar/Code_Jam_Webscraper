# -*- coding: utf-8 -*-

import sys

fn = sys.argv[1]
def gen_lines(fn):
    for lineRaw in open(fn, 'r').readlines():
        line = lineRaw[0:-1]
        yield line


gl = gen_lines(fn)

L,D,N = [int(sd) for sd in gl.next().split(' ')]

words = []
for n in xrange(D):
    words.append(gl.next())

patts = []
for n in xrange(N):
    patts.append(gl.next())

def setPatt(patt):
    sp = []
    left = patt
    while len(left) > 0:
        if not left[0] in ('(',')'):
            sp.append(set((left[0],)))
            left = left[1:]
        else:
            sub = left[1:left.index(')')]
            left = left[len(sub)+2:]
            sp.append(set(sub))
    return sp

def count(patt, words):
    sp = setPatt(patt)
    cnt = 0
    for w in words:
        match = True
        for i,c in enumerate(w):
            if not c in sp[i]:
                match = False
                break
        if match:
            cnt += 1
    return cnt

i = 1
for c in [count(patt,words) for patt in patts]:
    print "Case #%d: %d" % (i,c)
    i += 1

