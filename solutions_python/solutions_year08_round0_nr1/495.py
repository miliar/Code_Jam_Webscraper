
import operator
import sys

def get_furthest_engine(_queries, _engines, ignore=[]):
    if not _queries:
        return (None, 0)

    engines = set(_engines) - set(ignore)

    indexes = []
    for eng in engines:
        try:
            indexes.append((eng, _queries.index(eng)))
        except ValueError:
            return (eng, 0)

    indexes.sort(key=operator.itemgetter(1), reverse=True)

    return indexes[0]

def process(engines, queries):

    if not queries:
        return 0

    start_engine, start_point = get_furthest_engine(queries, engines)
        
    queries = queries[start_point:]
    engine = start_engine
    switch = 0

    for i in xrange(0, len(queries)):
        query = queries[i]
        if query == engine:
            switch += 1
            engine, _ignore = get_furthest_engine(queries[i+1:], engines, [engine])

    return switch

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print >>sys.stderr, 'No input file specified!'
        sys.exit(1)

    input = [line.strip('\n\r\n') for line in open(sys.argv[1]).readlines()]
    num_cases = int(input.pop(0))
    
    for i in xrange(0, num_cases):
        eng_count = int(input.pop(0))
        engines = input[:eng_count]
        input = input[eng_count:]
        query_count = int(input.pop(0))
        queries = input[:query_count]
        input = input[query_count:]

        print 'Case #%d: %d' % (i + 1, process(engines, queries))
