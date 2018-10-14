
def sol(A, B, K):
    r = 0
    for i in xrange(A):
        for j in xrange(B):
            if (i & j < K):
                r+= 1
            
    return r
    

import sys
readline = sys.stdin.readline

line = readline()
tn = int(line)
for i in xrange(1, tn + 1):
    A, B, K = map(int, readline().split(" "))
    print 'Case #{}: {}'.format(i, sol(A, B, K))
