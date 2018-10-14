import heapq
t = int(raw_input())
for kei in xrange(t):
    n, r, _, y, _, b, _ = [int(x) for x in raw_input().split()]
    q = []
    if r > 0:
        q.append([-r, -r, 'R'])
    if y > 0:
        q.append([-y, -y, 'Y'])
    if b > 0:
        q.append([-b, -b, 'B'])
    if len(q) == 1 or (len(q) == 2 and q[0][0] != q[1][0]):
        # print q
        # print 'wew1'
        print "Case #%d: IMPOSSIBLE" % (kei+1)
        continue
    res = []
    heapq.heapify(q)
    while q:
        # print q
        a1 = heapq.heappop(q)
        if q:
            res.append(a1[2])
            a2 = heapq.heappop(q)
            res.append(a2[2])
            a1[0] += 1
            a2[0] += 1
            if a1[0]:
                heapq.heappush(q, a1)
            if a2[0]:
                heapq.heappush(q, a2)
        else:
            for i in xrange(-a1[0]):
                res.append(a1[2])
            break
    # print q
    ok = True
    for i in xrange(n):
        if res[i-1] == res[i]:
            ok = False
            break
    if ok:
        print "Case #%d: %s" % (kei+1, ''.join(res))
    else:
        # print ''.join(res)
        print "Case #%d: IMPOSSIBLE" % (kei+1)
