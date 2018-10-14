import numpy
from string import ascii_lowercase

NWES = (
        (0,0),
        (-1,0),
        (0,-1),
        (0,1),
        (1,0),
        )


def basin(amap):
    h, w = amap.shape
    cmap = numpy.zeros((h,w), numpy.character)
    flowmap = numpy.zeros((h,w), numpy.int)

    def vadd(a,b):
        r = (a[0]+b[0], a[1]+b[1])
        if r[0]<0 or r[0]>=h or r[1]<0 or r[1]>=w:
            raise IndexError
        return r

    def flowto(a):
        return vadd(a, NWES[flowmap[a]])

    for i in range(h):
        for j in range(w):
            for k in range(1,5):
                p0 = flowto((i,j))
                try:
                    p = vadd((i,j), NWES[k])
                    if amap[p] < amap[p0]:
                        flowmap[i,j] = k
                except IndexError:
                    pass

    def connected(a, b):
        return flowto(a)==b or flowto(b)==a

    def flow(i,j, c):
        q=[(i,j)]
        cmap[i,j] = c
        while q:
            p = q.pop(0)
            for dir in NWES[1:]:
                try:
                    np = vadd(dir, p)
                    if cmap[np]:
                        continue
                except IndexError:
                    continue
                if connected(p, np):
                    q.append(np)
                    cmap[np] = c
        return

    cs = iter(ascii_lowercase)
    for i in range(h):
        for j in range(w):
            if not cmap[i,j]:
                flow(i,j, cs.next())
    return cmap

def slovemap(f):
    h, w = [int(x) for x in f.readline().split()]
    m = numpy.zeros((h,w), numpy.int)
    for i in range(h):
        m[i] = [int(x) for x in f.readline().split()]
    s = basin(m)
    for i in s:
        print ' '.join(i)
    return

def main(infn):
    f = open(infn)
    t = int(f.readline().strip())
    for i in range(t):
        print "Case #%d:"%(i+1)
        slovemap(f)
    return

import sys
main(*sys.argv[1:])



