for case in xrange(input()): # cases
    search_engines = {}
    for i in xrange(input()): # search engines
        search_engines[raw_input()] = 0
    queries = []
    for i in xrange(input()): # queries
        queries.append(raw_input())
    for query in queries:
        if search_engines.has_key(query):
            search_engines[query] = 100000 # Impossible to reach 100000
            search_engines[query] = min(search_engines.values()) + 1
    print 'Case #' + str(case + 1) + ":", min(search_engines.values())