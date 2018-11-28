from sys import stdin

tno = int(stdin.readline())
for i in xrange(0, tno):
    hm = 0
    tt = int(stdin.readline())
    an, bn = map(int, stdin.readline().split())
    def ptime(s):
        h, m = map(int, s.split(":"))
        return 60*h + m
    def add(fl, tl):
        d1, d2 = map(ptime, stdin.readline().split())
        fl.append((d1, 1,))
        tl.append((d2+tt, -1,))
    alist = []
    blist = []
    for _ in xrange(0, an):
        add(alist, blist)
    for _ in xrange(0, bn):
        add(blist, alist)
    def count(l):
        l.sort()
        y, z = 0, 0
        for _, x in l:
            y += x
            z = max(y, z)
        return z
    print "Case #%d: %d %d"%(i+1, count(alist), count(blist),)
