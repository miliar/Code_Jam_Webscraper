__author__ = 'Alen'

import sys

def war(ls1, ls2):
    i = 0
    w = 0
    for k in ls1:
        if i < len(ls2):
            if ls2[i] > k:
                continue
            else:
                i += 1
                w += 1

        else:
            break
    return w


N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
    print 'Case #%d:' % qw,

    n = int(sys.stdin.readline())

    ks1 = sys.stdin.readline().strip().split(' ')
    ks2 = sys.stdin.readline().strip().split(' ')
    ks1.sort()
    ks2.sort()

    r1 = war(ks1, ks2)
    r2 = n - war(ks2, ks1)
    print r1, r2