def process(engines, queries):
    # C[k,s] = (Number of minimal switches for queries[0:k] with last engine is s)
    #
    # C[0,s] = 0          -- of course,
    # C[k,s] for k > 0 = min { C[k-1,s0] + (s0 = s then 1 else 0) }
    table = [0] * len(engines)
    for query in queries:
        newtable = [min(table[i] + (engines[i] != newengine) for i in xrange(len(engines))
                        if engines[i] != query)
                    for newengine in engines]
        table = newtable
    return min(table)

import sys
next = iter(sys.stdin).next
ncases = int(next())
for i in xrange(ncases):
    nengines = int(next())
    engines = [next().rstrip('\r\n') for j in xrange(nengines)]
    nqueries = int(next())
    queries = [next().rstrip('\r\n') for j in xrange(nqueries)]
    minswitch = process(engines, queries)
    print 'Case #%d: %d' % (i+1, minswitch)

