from sys import stdin

tno = int(stdin.readline())
for i in xrange(0, tno):
    hm = 0
    sno = int(stdin.readline())
    ss = set()
    for _ in xrange(0, sno):
        name = stdin.readline().strip()
        ss.add(name)
    qno = int(stdin.readline())
    s = set()
    for j in xrange(0,qno):
        name = stdin.readline().strip()
        if name in ss:
            s.add(name)
        if len(s) == sno:
            hm += 1
            s = set((name,))
    print "Case #%d: %d"%(i+1,hm,)
