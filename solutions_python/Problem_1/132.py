import sys
f = sys.stdin
n = int(f.readline())
for case in range(1, n+1):
    s = int(f.readline())
    search_engines = []
    for i in range(s):
        search_engine = f.readline().strip()
        search_engines.append(search_engine)
    q = int(f.readline())
    queries = []
    for i in range(q):
        query = f.readline().strip()
        queries.append(query)
    switch = 0
    i = 0
    while i < q:
        table = set(search_engines)
        while i < q:
            query = queries[i]
            if query in table:
                table.remove(query)
                if not table:
                    switch += 1
                    break
            i += 1
    print 'Case #%d: %d' % (case, switch)
