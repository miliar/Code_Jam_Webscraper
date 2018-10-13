#!/usr/bin/python

import sys, math

def saveTheUniverse(engines, queries):
    count = 0
    while(queries):
        best = 0
        for e in engines:
            if e in queries:
                best = max(best, queries.index(e))
            else:
                return count
        queries = queries[best:]
        count += 1
    return count

if __name__=="__main__":
    fpin=open(sys.argv[1])
    if len(sys.argv) > 2:
        fpout = open(sys.argv[2], 'w')
    else:
        fpout = sys.stdout


    cases = int(fpin.readline().strip())
    for case in range(1,cases+1):
        engines = []
        queries = []
        numEngines = int(fpin.readline().strip())
        for e in range(numEngines):
            engines.append(fpin.readline().strip())
        numQueries = int(fpin.readline().strip())
        for q in range(numQueries):
            queries.append(fpin.readline().strip())
        fpout.write("Case #%d: %s\n" % (case, saveTheUniverse(engines, queries)))

