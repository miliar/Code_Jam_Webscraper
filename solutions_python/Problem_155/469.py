#/usr/bin/cython --embed -2 A.pyx
#/usr/bin/gcc -o A -I/usr/include/python2.7 A.c /usr/lib/x86_64-linux-gnu/libpython2.7.so
#./A
import sys

def q():
    N, sl = sys.stdin.readline().split()
    N = int(N)
    sl = map(int, sl)
    c = 0
    r = 0
    for i in range(1, N+1):
        c += sl[i-1]
        if c < i:
            r += i - c
            c = i
    return r


T = int(sys.stdin.readline())
for t in range(T):
    ret = q()
    print 'Case #%d: %s' % (t+1, ret)
    print >>sys.stderr, 'Case #%d: %s' % (t+1, ret)
