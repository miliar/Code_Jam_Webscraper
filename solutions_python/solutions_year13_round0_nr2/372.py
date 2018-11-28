#/usr/bin/cython --embed -2 B.pyx
#/usr/bin/gcc -o B -I/usr/include/python2.7 B.c /usr/lib/libpython2.7.so
#./B

import sys

cdef q():
    cdef int N, M, n, m, t, a, r
    cdef int A[100][100]
    
    N,M = map(int, sys.stdin.readline().split())
    for n in range(N):
        m = 0
        for a in map(int, sys.stdin.readline().split()):
            A[n][m] = a
            m += 1
    
    #pm = [ [ A[n][m] for m in range(M) ] for n in range(N) ]
    #print >>sys.stderr, pm

    for n in range(N):
        for m in range(M):
            a = A[n][m]
            
            r = 0
            for t in range(N):
                if a < A[t][m]: 
                    r = 1
                    break
            if r == 0: continue
            
            for t in range(M):
                if a < A[n][t]: 
                    return 'NO'
    return 'YES'
    
T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %s' % (t+1, q())
    