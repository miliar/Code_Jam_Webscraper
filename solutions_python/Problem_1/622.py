def calc_switch(count, engines, queries):
    try:
        index = [queries.index(engine) for engine in engines]
    except:
        return count

    queries[0:max(index)] = []
    temp = count + 1
        

    return calc_switch(temp, engines, queries)

cases = int(raw_input())
for x in xrange(cases):
    num_engines = int(raw_input())
    engines = []
    for i in xrange(num_engines):
        engines.append(raw_input())
    num_queries = int(raw_input())
    queries = []
    for i in xrange(num_queries):
        queries.append(raw_input())
    print 'Case #' + str(x+1) + ': ' + str(calc_switch(0, engines, queries))
