def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        D, N = map(int, raw_input().split())
        horses = [None]*N
        for i in xrange(N): 
            horses[i] = map(int, raw_input().split())
        horses = sorted(horses)
        intersections = set()
        for i in xrange(N):
            ki, si = horses[i]
            tx = (D-ki) * 1.0 / si
            kx = ki + si * tx
            intersections.add((kx, tx))
            for j in xrange(i+1, N):
                kj, sj = horses[j]
                if si > sj:
                    tx = (kj-ki) * 1.0 / (si-sj)
                    kx = ki + si * tx
                    if kx > D: continue
                    intersections.add((kx, tx))
        res =  min(k/t for k,t in intersections)
        print 'Case #%d: %0.6f' % (_tc+1, res)
f()

