#!/usr/bin/python

f = open("input.txt")

n = int(f.readline())

for i in range(n):
    candn = int(f.readline())
    candv = map(int, f.readline().split())
    if reduce(lambda x,y: x ^ y, candv) == 0:
        print 'Case #%d: %d' % (i+1, sum(candv) - min(candv))
    else:
        print 'Case #%d: NO' % (i+1)
