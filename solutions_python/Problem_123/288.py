#/usr/bin/cython --embed -2 A.pyx
#/usr/bin/gcc -o A -I/usr/include/python2.7 A.c /usr/lib/libpython2.7.so
#./A

import sys

def p(A, V):
    i = 0
    while i<len(V):
        if A > V[i]:
            A += V[i]
            i += 1
            continue
        break
    if i>= len(V): return 0
    if A == 1: return len(V)-i
    c = 0
    while A<=V[i]:
        A += A-1
        c += 1
    if c >= len(V)-i: return len(V)-i
    return min(len(V)-i, c + p(A, V[i:]))
    

def q():
    A,N = map(int, sys.stdin.readline().split())
    V = map(int, sys.stdin.readline().split())
    
    V.sort()
    c = p(A, V)
    if c>0 and c!=len(V):
        sys.stderr.write('%s %s %d\n' % (A, V, c))
    return c



T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %d' % (t+1, q())
    