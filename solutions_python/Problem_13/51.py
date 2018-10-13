#!/usr/bin/env python

import logging
import extremes

INPUT_FILENAME = "A-small-attempt0.in"
INPUT_FILENAME = "A-large.in"

cache = {}
beforeLeafs = None

I_G, I_C, I_VALUE = range(3)

def readTree(M, input):
    nodes = []
    for i in range(M):
        if i <= beforeLeafs:
            G, C = [int(v) for v in input.readline().split()]
            value = None
        else:
            value = int(input.readline().strip())
        node = (G, C, value)
        nodes.append(node)
    return nodes

def minChanges(tree, root, M, wanted):
    node = tree[root]
    if root > beforeLeafs:
        if node[I_VALUE] != wanted:
            return extremes.uMax
        return 0

    key = (root, wanted)
    if key in cache:
        return cache[key]
    left = 2*(root + 1) - 1
    right = left + 1
    #TODO: prune
    l0 = minChanges(tree, left, M, 0)
    l1 = minChanges(tree, left, M, 1)
    r0 = minChanges(tree, right, M, 0)
    r1 = minChanges(tree, right, M, 1)

    result = None
    if wanted:
        if node[I_G]:
            result = l1 + r1
            if node[I_C]:
                result = min(result, 1 + l1, 1 + r1)
        else:
            result = min(l1, r1)
    else:
        if node[I_G]:
            result = min(l0, r0)
        else:
            result = l0 + r0
            if node[I_C]:
                result = min(result, 1 + l0, 1 + r0)

    cache[key] = result
    return result

def main():
    global cache
    global beforeLeafs
    input = file(INPUT_FILENAME)
    numCases = int(input.readline())
    for i in range(numCases):
        cache = {}
        M, V = [int(v) for v in input.readline().split()]
        beforeLeafs = (M - 1)//2 - 1
        tree = readTree(M, input)
        result = minChanges(tree, 0, M, V)
        if result == extremes.uMax:
            result = "IMPOSSIBLE"
        print "Case #%s: %s" % (i + 1, result)

if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    try:
        import psyco
        #psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

