import sys
input = sys.stdin.readline

for i in xrange(int(input())):
    n, d = input().split()
    p = 0
    z = 0
    for s, k in enumerate(map(int, d)):
        if p < s:
            z += 1
            p += 1
        p += k
    print 'Case #%d: %d' % (i+1, z)