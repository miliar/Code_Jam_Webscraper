import sys

f = open('B-large.in')

T = int(f.readline())
for i in range(T):
    D = int(f.readline())
    array = f.readline().split()
    p = [int(x) for x in array]
    m = max(p)
    best = m
    for max_slice in range(1, m):
        cur = 0
        for x in p:
            cur += (x-1)/max_slice
        cur += max_slice
        if cur < best:
            best = cur
    print 'Case #{0}: {1}'.format(i+1, best)
