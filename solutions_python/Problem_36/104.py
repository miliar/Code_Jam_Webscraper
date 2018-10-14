import numpy

W = 'welcome to code jam'
lw = len(W)

def calc(s):
    ls = len(s)
    n = numpy.zeros((ls+1, lw+1), numpy.int)
    for i in range(ls+1):
        n[i,0] = 1

    for i in range(1, ls+1):
        for j in range(1, lw+1):
            n[i,j] = n[i-1,j]
            if s[i-1]==W[j-1]:
                n[i,j]+=n[i-1,j-1]
            n[i,j] %= 10000
    return n[ls, lw]

def main(infn):
    f = open(infn)
    n = int(f.readline().strip())
    for i in range(n):
        s = f.readline().strip()
        r = calc(s)
        print 'Case #%d: %04d'%(i+1, r)

import sys
main(*sys.argv[1:])

