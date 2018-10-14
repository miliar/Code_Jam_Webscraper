import sys

f = open(sys.argv[1])

o = open(sys.argv[1].split('.')[0] + '.out', 'w')

nCases = int(f.readline().strip())

for case in range(nCases):
    nEngines = int(f.readline().strip())
    engines = []
    for engine in range(nEngines):
        engines.append(f.readline().strip())
        
    nQueries = int(f.readline().strip())

    queries = []
    for query in range(nQueries):
        queries.append(f.readline().strip())

    switches = -1

    while queries:
        next_engine_query = [queries.index(engine) for engine in engines if engine in queries]

        if len(next_engine_query) != len(engines):
            switches += 1
            break

        current_query_idx = max(next_engine_query)
    
        queries = queries[current_query_idx:]
        switches += 1

    if switches < 0:
        switches = 0

    o.write('Case #%d: %d\n' % (case + 1, switches))
