#/usr/bin/cython --embed -2 B.pyx
#/usr/bin/gcc -o B -I/usr/include/python2.7 B.c /usr/lib/x86_64-linux-gnu/libpython2.7.so
#./B
import sys


def init():
    ps = {}
    for x in range(1, 1010):
        ps[x] = []
        for n in range(1, x+1):
            c = x / n
            if x%n == 0: c -= 1
            if len(ps[x])==0 or ps[x][-1][0] != c:
                ps[x].append((c, n))
        ps[x].reverse()
#        print >>sys.stderr, '%d %s' % (x, ps[x])
    return ps

ps = init()

def q():
    D = int(sys.stdin.readline())
    P = map(int, sys.stdin.readline().split())

    c = max(P)
    mcnt = c
    while c>0:
        cnt = c
        for p in P:
            for z in ps[p]:
                if z[1] <= c:
                    cnt += z[0]
                    break
        if cnt < mcnt: mcnt = cnt
        c -= 1
    return mcnt
    


T = int(sys.stdin.readline())
for t in range(T):
    ret = q()
    print 'Case #%d: %s' % (t+1, ret)
    print >>sys.stderr, 'Case #%d: %s' % (t+1, ret)
