import sys
from bisect import bisect_left

from datetime import time

def start_from(l, d, sgn, x):
    result[sgn] += 1
    side = l
    sided = d
    i = 0
    while(i < len(side)):
        t1 = None
#        print a, b, side
        if side is a:
            t1 = a.pop(i)
#            print 'jestem w a'
        elif side is b:
            t1 = b.pop(i)
#            print 'jestem w b'
#        print '$'*100
#        t1 = side.pop(i)
#        print a, b, side
#        print '#'*10, 'a:', len(a), 'b:', len(b)
        t = sided[t1]
#        print 'czas: ', t1, t
        h = t.hour
        m = t.minute
        h = (h + ((m + x) / 60)) % 24
        m = (m + x) % 60
        t = time(h, m)
#        print 'prawdziwy odjazd: ', t
        if side is a:
            side = b
            sided = bd
        elif side is b:
            side = a
            sided = ad
        i = bisect_left(side, t)
        if i >= len(side) or side[i] < t:
            break
#        else:
#            print 'bisect: ', side[i]


n = int(sys.stdin.readline())
for c in range(n):
    a, b = [], []
    ad, bd = {}, {}
    t = int(sys.stdin.readline())
    na, nb = [int(x) for x in sys.stdin.readline().strip().split()]

    for i in range(na):
        start, finish = sys.stdin.readline().split()
        h, m = [int(x) for x in start.split(':')]
        t1 = time(h, m)
        h, m = [int(x) for x in finish.split(':')]
        t2 = time(h, m)
        a.append(t1)
        ad[(t1)] = t2
    for i in range(nb):
        start, finish = sys.stdin.readline().split()
        h, m = [int(x) for x in start.split(':')]
        t1 = time(h, m)
        h, m = [int(x) for x in finish.split(':')]
        t2 = time(h, m)
        b.append(t1)
        bd[t1] = t2
    a.sort()
    b.sort()
    #print a, b
    result = {'a' : 0, 'b' : 0}
    while len(a) > 0 and len(b) > 0:
#        print '*'*100
        if a[0] < b[0]:
            start_from(a, ad, 'a', t)
        else:
            start_from(b, bd, 'b', t)
#    print len(a), len(b)
    result['a'] += len(a)
    result['b'] += len(b)

    print "Case #%d: %d %d" % ((c+1), result['a'], result['b'])

