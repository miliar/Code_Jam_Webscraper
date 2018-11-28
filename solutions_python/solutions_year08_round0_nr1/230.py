#!/usr/bin/python
import sys


if  __name__ == "__main__":
    testCases = int(sys.stdin.readline())
    for c in range(1, testCases + 1):
        numEngines = int(sys.stdin.readline())
        for e in range(numEngines):
            eng = sys.stdin.readline()
        numQueries = int(sys.stdin.readline())
        seen = set()
        count = 0
        res = 0
        for q in range(numQueries):
            query = sys.stdin.readline().strip()
            if query not in seen:
                count +=1
                seen.add(query)
            if count == numEngines:
#                print "%d: Ran with %s" % (q, query)
                res += 1
                count = 1
                seen = set([query])
        print "Case #%d: %d" % (c, res)




