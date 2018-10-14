import sys

f = sys.stdin

t = int(f.readline())
for i in xrange(t):
    a, b, k = map(int, f.readline().split())
    
    w = 0
    for x in xrange(a):
        for y in xrange(b):
            if x & y < k:
                w += 1
    print 'Case #%d: %d' % (i+1, w)
