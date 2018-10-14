
import sys, itertools



def get_count(queries, engines):
    # count how many times each query appears
    count = dict((query, queries.count(query)) for query in queries)
    return count


def get_blocks(queries, engines):
    # count how many blocks of repeated queries appear
    count = dict((name, 0) for name in engines)
    current = None
    for q in queries:
        if q != current:
            count[q] += 1
            current = q
    return count


def get_distance(queries, engines):
    # count how far a query first ocurrence is from the origin
    distance = dict((name, None) for name in engines)

    for i, q in enumerate(queries):
        if distance[q] is None:
            distance[q] = i

    # replace None for the max distance
    for k in distance:
        if distance[k] is None:
            distance[k] = len(queries)
    return distance

    
def get_switches(queries, engines):
    # so, if queries is empty, no switch is needed, return 0
    if not queries:
        return 0
    
    # otherwise, count number of blocks
    blocks = get_blocks(queries, engines)
    blockscount = blocks.items()
    blockscount.sort(key=lambda b: b[1])

    # if some query never appears, no switch needed
    if blockscount[0][1] == 0:
        return 0

    # if two or more queries appear only once, one switch needed
    if blockscount[0][1] == blockscount[1][1] == 1:
        return 1

    # in other cases, let's count it the hard way...

    # start it
    current = None
    switches = -1
    for i, query in enumerate(queries):
        # for the start query and all nedeed switches...
        if current is None or current == query:
            # get queries distances from origin and blocks
            dist = get_distance(queries[i:], engines)
            blocks = get_blocks(queries[i:], engines)
            # order engines to get the farther away from origin and
            # with least blocks... hope timsort is stable
            engines.sort(key=lambda x: blocks[x])
            engines.reverse()
            engines.sort(key=lambda x: dist[x])
            # last engine different from query should be the best
            for eng in reversed(engines):
                if eng != current and eng != query:
                    current = eng
                    break
            else:
                raise ValueError("cannot find engine")
            switches += 1
            
    return switches



def main():
    n = int(sys.stdin.readline())

    for i in xrange(n):
        # test case number
        x = i + 1

        # search engines number
        s = int(sys.stdin.readline())
        engines = [sys.stdin.readline().strip() for i in xrange(s)]

        # queries
        q = int(sys.stdin.readline())
        queries = [sys.stdin.readline().strip() for i in xrange(q)]

        switches = get_switches(queries, engines)
        
        print "Case #%d: %d"%(x, switches)

main()
