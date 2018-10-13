# coding: utf-8

for t in xrange(input()):
    n = input()
    ps = []
    for i in xrange(n):
        ai,bi = map(int, raw_input("").split())
        ps.append((ai, bi))

    ps.sort(key=lambda x: x[0])
    #print ps
    cnt = 0
    for i in xrange(len(ps)):
        p,q = ps[i]
        for j in xrange(i+1, len(ps)):
            r,s = ps[j]
            if s < q:
                #print "count!",p,q,r,s
                cnt += 1
    print "Case #%d: %d" % (t+1, cnt)
