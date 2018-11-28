#/usr/bin/cython --embed -2 C.pyx
#/usr/bin/gcc -o C -I/usr/include/python2.7 C.c /usr/lib/x86_64-linux-gnu/libpython2.7.so
#./C
import sys

mult = {
    -4 : { -4: -1, -3: -2, -2: 3, -1: 4, 1: -4, 2: -3, 3: 2, 4: 1},
    -3 : { -4: 2, -3: -1, -2: -4, -1: 3, 1: -3, 2: 4, 3: 1, 4: -2},
    -2 : { -4: -3, -3: 4, -2: -1, -1: 2, 1: -2, 2: 1, 3: -4, 4: 3},
    -1 : { -4: 4, -3: 3, -2: 2, -1: 1, 1: -1, 2: -2, 3: -3, 4: -4},
    1 : { -4: -4, -3: -3, -2: -2, -1: -1, 1: 1, 2: 2, 3: 3, 4: 4},
    2 : { -4: 3, -3: -4, -2: 1, -1: -2, 1: 2, 2: -1, 3: 4, 4: -3},
    3 : { -4: -2, -3: 1, -2: 4, -1: -3, 1: 3, 2: -4, 3: -1, 4: 2},
    4 : { -4: 1, -3: 2, -2: -3, -1: -4, 1: 4, 2: 3, 3: -2, 4: -1},
}


def q():
    global L, X, ss, cache

    L,X = map(int, sys.stdin.readline().split())
    ss = sys.stdin.readline().strip()
    if L*X < 3: return 'NO'
  
    sv = []
    v = 1
    for s in ss:
        v = mult[v][ '01ijk'.index(s) ]
        sv.append(v)

    for x in range(X-1):
        v = mult[v][ sv[-1] ]

    if v != mult[ mult[2][3] ][4]: return 'NO'

    e1 = 2
    e2 = mult[2][3]
    for x in range(X):
        for i in range(L):
            if e1 != 0 and sv[i] == e1:
                e1 = 0
            if e1 == 0 and e2 != 0 and sv[i] == e2:
                return 'YES'
        for i in mult.keys():
            if mult[ sv[-1] ][i] == e1:
                e1 = i
                break
        for i in mult.keys():
            if mult[ sv[-1] ][i] == e2:
                e2 = i
                break

    return 'NO'
                            


T = int(sys.stdin.readline())
for t in range(T):
    ret = q()
    print 'Case #%d: %s' % (t+1, ret)
    print >>sys.stderr, 'Case #%d: %s' % (t+1, ret)
