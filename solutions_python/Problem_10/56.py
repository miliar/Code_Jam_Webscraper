#!/usr/bin/env python

import logging

#INPUT_FILENAME = "A-small-attempt0.in"
INPUT_FILENAME = "A-large.in"

def calcPresses(args, counts):
    P, K, L = args
    if L > K * P:
        return "Impossible"

    counts.sort(reverse=True)
    presses = 0
    for i, count in enumerate(counts):
        times = (i // K) + 1
        presses += count * times
    return presses

def main():
    input = file(INPUT_FILENAME)
    numCases = int(input.readline())
    for i in range(numCases):
        args = [int(v) for v in input.readline().split()]
        counts = [int(v) for v in input.readline().split()]
        result = calcPresses(args, counts)
        print "Case #%s: %s" % (i + 1, result)

if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

