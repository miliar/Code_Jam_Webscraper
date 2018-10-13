#!/usr/bin/env python
from sets import Set

def distinctValues(l):
    return list(Set(l))

def memoize(f):
    d = {}
    def g(*args):
        if args not in d:
            d[args] = f(*args)
#        print `args` + "##" + `d[args]`
        return d[args]
    return g

@memoize
def doDynamic(engines, queries, currEngine):
    if currEngine is None:
        minV = 3000
        for i in engines:
            s = doDynamic(engines, queries, i)
            if s < minV: minV = s
        return minV
    if len(queries) == 1:
        if currEngine == queries[0]: return 1
        return 0
    if currEngine == queries[0]:
        minV = 3003
        qs = queries[1:]
        for i in Set(engines).difference((currEngine,)):
            s = doDynamic(engines, qs, i)
            if s < minV: minV = s
        return minV + 1
    else:
        minV = 3004
        qs = queries[1:]
        for i in engines:
            s = doDynamic(engines, qs, i)
            if i != currEngine: s += 1
            if s < minV: minV = s
        return minV

def main(engines, queries):
    S = len(engines)
    distinct = distinctValues(queries)
    qS = len(distinct)
    if qS == S:
        return doDynamic(engines, queries, None)
    if qS < S:
        return 0
    if qS > S:
        #should not ever happen
        return -1

if __name__ == "__main__":
    N = int(raw_input())
    replies = []
    for tests in range(N):
        S = int(raw_input())
        engineList = []
        for engines in range(S):
            engineList.append(raw_input())
        Q = int(raw_input())
        queryList = []
        for queries in range(Q):
            queryList.append(raw_input())
        replies.append("Case #" + str(tests+1) + ": " + str(main(tuple(engineList),tuple(queryList))))
    print "\n".join(replies)
