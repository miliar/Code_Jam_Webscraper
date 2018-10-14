fin = open('in', 'r')
test_count = int(fin.readline().rstrip())
for tn in xrange(test_count):
    p = int(fin.readline().rstrip())
    m = [int(x) for x in fin.readline().rstrip().split()]

    r = [{x: 0} for x in m]
    while len(r) > 1:
        cur = []
        costs = [int(x) for x in fin.readline().rstrip().split()]
        for i in xrange(len(costs)):
            dc = {}
            for a, b in r[2*i].items():
                for c, d in r[2*i+1].items():
                    x = min(a, c)
                    y = b + d
                    if x not in dc:
                        dc[x]=y+costs[i]
                    else:
                        dc[x]=min(dc[x], y+costs[i])
                    if x > 0:
                        if x-1 not in dc:
                            dc[x-1]=y
                        else:
                            dc[x-1]=min(dc[x-1], y)
            cur.append(dc)
        r = cur

    print 'Case #%d: %d' % (tn+1, min(r[0].values()))
