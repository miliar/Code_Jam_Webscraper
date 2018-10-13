#!/usr/bin/python

def cases(input):
    ncases = int(input.readline().strip())

    while ncases > 0:
        engines, queries = [], []
        s = int(input.readline().strip())
        while s > 0:
            engines.append(input.readline().strip())
            s -= 1
        q = int(input.readline().strip())
        while q > 0:
            queries.append(input.readline().strip())
            q -= 1
        yield (tuple(engines), queries)
        ncases -= 1

def solve(engines, queries):
    if len(queries) == 0:
        return 0

    switches = -1
    while len(queries) > 0:
        switches += 1
        notin = tuple(x for x in engines if x not in queries)
        if notin:
#             print notin
            break
        next = sorted((queries.index(x), x) for x in engines if x in queries)

#         print next[-1][1]
        queries = queries[next[-1][0]:]

    return switches

if __name__ == '__main__':
    import sys

    for n, case in enumerate(cases(sys.stdin)):
        print "Case #%d: %d" % (n + 1, solve(*case))
