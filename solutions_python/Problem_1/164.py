#!/usr/bin/python

def read_input():
    n = int(raw_input())
    cases = []
    for i in xrange(n):
        s = int(raw_input())
        engines = [ raw_input() for j in xrange(s) ]
        q = int(raw_input())
        queries = [ raw_input() for j in xrange(q) ]
        cases.append( (engines, queries) )
    return cases

def count(engines, queries):
    d = dict( (engine, 0) for engine in engines )
    for query in queries:
        d_query = d.get(query)
        if d_query is not None:
            d[query] = d_query + 1
    return sorted((v, k) for (k, v) in d.iteritems())

def count2(engines, queries):
    c = 0
    s = set(engines)
    for query in queries:
        if query in s:
            s.remove(query)
        if not s:
            s = set(engines)
            if query in s:
                s.remove(query)
            c += 1
    return c

def main():
    cases = read_input()
    i = 1
    for engines, queries in cases:
        print 'Case #%d: %d' % (i, count2(engines, queries))
        i += 1

if __name__ == '__main__':
    main()
