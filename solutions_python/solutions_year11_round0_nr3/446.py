# -*- coding:utf-8 -*-
import sys

def solve(n, l):
    xor_sum = reduce(lambda x,y: y ^ x, l)
    if xor_sum != 0:
        return -1
    else:
        return sum(l[1:])

if __name__=='__main__':
    fname = sys.argv[1]
    f = open(fname)

    t = int(f.readline().strip())
    for i in range(t):
        n = int(f.readline().strip())
        l = map(lambda x:int(x), f.readline().strip().split(' '))
        l.sort()
        t = solve(n,l)
        if t == -1:
            print "Case #%d: NO" % (i+1,)
        else:
            print "Case #%d: %d" % (i+1, t)
