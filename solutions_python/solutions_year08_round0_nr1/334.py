#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

FILE = 'A-large.in'
#FILE = 'teste_saving_2'
#recursive try
def get_changes(e, q, i):
    if maxq == i:
        return 0
    while maxq > i and q[i] != e:
        i += 1
    if maxq > i and q[i] == e:
        value = 9999999
        for n in engines:
            if e != n:
                value = min(value, get_changes(n, q, i))
        return value +1
    else:
        return 0

def smart_changes(e, i):
    last = None
    bool = True
    points = 0
    while bool:
        while i < maxq and e:
            if queries[i] in e:
                e.remove(queries[i])
            last = (queries[i], i) 
            i += 1
        if not e:
            i -= 1
    #    print i, last
        if last and i < maxq:
            e = engines[:]
            e.remove(last[0])
            points += 1
        else:
            bool = False
    return points

def choose_best_():
    changes = []
    for engine in engines:
        changes += [get_changes(engine, queries, 0)]
    changes.sort()
    return changes[0]

def choose_best():
    return smart_changes(engines[:], 0)

lines = [] 
for line in file(FILE).readlines():
    lines += [line.replace("\n", "").replace("\t", "")]

i = 1
N = int(lines.pop(0))
for case in range(N):
    S = int(lines.pop(0))
    engines = []
    for se in range(S):
        engines += [lines.pop(0)]
    Q = int(lines.pop(0))
    queries = []
    for q in range(Q):
        queries += [lines.pop(0)]
    maxq = len(queries)
    print "Case #%d: %d"%(i, choose_best())
    i += 1


