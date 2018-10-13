#/usr/bin/cython --embed -2 A.pyx
#/usr/bin/gcc -o A -I/usr/include/python2.7 A.c /usr/lib/libpython2.7.so
#./A

import sys

cdef q():
    cdef int m[4][4]
    cdef int i, j, v
    for i in range(4):
        j = 0
        for ch in sys.stdin.readline():
            v = '.OXT'.find(ch)
            if v < 0: continue
            m[i][j] = v
            j += 1
    sys.stdin.readline()
    
    pm = [ [ m[i][j] for j in range(4) ] for i in range(4) ]
    print >>sys.stderr, pm
    
    for i in range(4):
        v = m[i][0]
        for j in range(1,4):
            v &= m[i][j]
        if v>0: return '%s won' % '.OX'[v]

        v = m[0][i]
        for j in range(1,4):
            v &= m[j][i]
        if v>0: return '%s won' % '.OX'[v]
        
    v = m[0][0]
    for i in range(1,4):
        v &= m[i][i]
    if v>0: return '%s won' % '.OX'[v]
    
    v = m[3][0]
    for i in range(1,4):
        v &= m[3-i][i]
    if v>0: return '%s won' % '.OX'[v]
    
    v = 0
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: v += 1
    if v>0: return 'Game has not completed'
    return 'Draw'
        
        
T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %s' % (t+1, q())
    