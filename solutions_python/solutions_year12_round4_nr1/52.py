#!/usr/bin/env python
import sys

T = int(raw_input())
for t in xrange(T):

    N = int(raw_input())
    sys.stderr.write("Case #%d - %d\n" % (t+1, N))
    d = []
    l = []
    for n in xrange(N):
        a, b = map(int, raw_input().split())
        d.append(a)
        l.append(b)
    D = int(raw_input())
    d.append(D)
    l.append(0)

    sys.stderr.write(str(d)+"\n")
    sys.stderr.write(str(l)+"\n")

    res = 'NO'
    q = []
    p = set( [0] ) # vine
    q.append( (0,0) ) # pos, vine
    while q:
        pos, vine = q.pop(0)
        if pos >= D:
            res = 'YES'
            break

        for i in xrange(vine+1, len(d)):
            if d[i] - d[vine] <= d[vine] - pos:
                # swing
                cur_pos = max(d[vine], d[i]-l[i])
                cur_vine = i
                if cur_vine not in p:
                    q.append( (cur_pos, cur_vine) )
                    p.add( cur_vine )

    print "Case #%d: %s" % (t+1, res)


