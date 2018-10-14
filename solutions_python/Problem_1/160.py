def minSwitches(engines,queries):
    switches = 0
    cur = ""
    try:
        while len(queries) > 0:
            maxim = 0
            maxeng = ""
            for engine in engines:
                if queries.index(engine) > maxim  and engine != cur:
                    maxim = queries.index(engine)
                    maxeng = engine
            cur = maxeng
            queries = queries[maxim:]
            switches += 1
    except ValueError : return switches
    return switches

n = int(raw_input())
for z in xrange(n):
    m = int(raw_input())
    engines = []
    for y in xrange(m):
        engines.append(raw_input())
    m = int(raw_input())
    searches = []
    for y in xrange(m):
        searches.append(raw_input())
    print "Case #%d: %d" % (z+1,minSwitches(engines,searches))
