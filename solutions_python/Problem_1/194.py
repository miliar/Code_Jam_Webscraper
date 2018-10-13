#!/usr/bin/env python

import logging
import extremes

#INPUT_FILENAME = "A-small-attempt0.in"
INPUT_FILENAME = "A-large.in"

def readInput(input):
    engines = []
    numEngines = int(input.readline())
    for i in range(numEngines):
        engines.append(input.readline())

    queries = []
    numQueries = int(input.readline())
    for i in range(numQueries):
        queries.append(input.readline())
    return engines, queries

cache = None
def optimize(engines, queries, nextUsed):
    global cache
    if len(queries) == 1:
        return 1 if queries[0] == nextUsed else 0

    key = (len(queries), nextUsed)
    if key in cache:
        return cache[key]

    minChanges = extremes.uMax
    for e in engines:
        if e == queries[-1]:
            continue
        numChanges = optimize(engines, queries[:-1], e)
        if e != nextUsed:
            numChanges += 1
        minChanges = min(minChanges, numChanges)
    cache[key] = minChanges
    return minChanges

def main():
    global cache
    input = file(INPUT_FILENAME)
    numCases = int(input.readline())
    for i in range(numCases):
        cache = {}
        engines, queries = readInput(input)
        if len(queries) == 0:
            minSwitches = 0
        else:
            minSwitches = extremes.uMax
            for e in engines:
                minSwitches = min(minSwitches, optimize(engines, queries, e))
        print "Case #%s: %s" % (i + 1, minSwitches)

if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

