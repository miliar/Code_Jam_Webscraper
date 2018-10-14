#!/usr/bin/python

def solve(search_engines, queries, start):
    if start == len(queries):
        return 0
    ranges = [0 for search_engine in search_engines]
    found = []
    for query in queries[start:]:
        for i, search_engine in enumerate(search_engines):
            if search_engine not in found:
                if query != search_engine:
                    ranges[i] += 1
                else:
                    found.append(search_engine)
    if start == 0:
        return 0 + solve(search_engines, queries, start + max(ranges))
    else:
        return 1 + solve(search_engines, queries, start + max(ranges))

f = open('A-small-attempt0.in')
data = f.read().split('\n')
f.close()

for i in xrange(int(data.pop(0))):
    search_engines = []
    for j in xrange(int(data.pop(0))):
        search_engines.append(data.pop(0))
    queries = []
    for j in xrange(int(data.pop(0))):
        queries.append(data.pop(0))
    print 'Case #%s: %s' % (i + 1, solve(search_engines, queries, 0))
