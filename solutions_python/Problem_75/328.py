#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def makeret(r):
    if len(r) == 0:
        return "[]"
    ret = '['
    for c in r:
        ret += c + ", "
    ret = ret[:-2] + "]"
    return ret

def combine(es, c):
    ori = [ x for x in es ]
    bs = c[:2]
    nb = c[-1]
    es = es[-2:]
    for b in bs:
        if b not in es:
            break
        es.remove(b)
    else:
        ori = ori[:-2]
        ori.append(nb)
        return ori
    return ori

def oppose(es,d):
    ori = [ x for x in es]
    for de in d:
        if de not in es:
            break
        es.remove(de)
    else:
        return []
    return ori

def solve(cs, ds, n):
    es = []
    for e in n:
        es += e
        for c in cs:
            es = combine(es,c)
        for d in ds:
            es = oppose(es,d)
    return makeret(es)

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        line = raw_input().split()
        nc = int(line[0])
        cs = line[1:1+nc]
        nd = int(line[1+nc])
        ds = line[1+nc+1:1+nc+1+nd]
        nn = int(line[1+nc+1+nd])
        n  = line[1+nc+1+nd+1]
        print "Case #%d: %s" % ( i+1, solve(cs, ds, n))
