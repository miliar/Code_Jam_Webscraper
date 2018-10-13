#!/usr/bin/env python

import logging

INPUT_FILENAME = "B-small-attempt0.in"
INPUT_FILENAME = "B-large.in"
#INPUT_FILENAME = "B-small.in"


def main():
    input = file(INPUT_FILENAME)
    num_cases = int(input.readline().rstrip())
    for case in xrange(1, num_cases + 1):
        N, K, B, T = [int(v) for v in input.readline().rstrip().split()]
        X = [int(v) for v in input.readline().rstrip().split()]
        V = [int(v) for v in input.readline().rstrip().split()]
        num_swaps = 0
        num_to_pick = 0
        while K > 0 and len(X) > 0:
            x = X.pop(-1)
            v = V.pop(-1)
            if v * T >= B - x:
                K -= 1
                num_swaps += num_to_pick
            else:
                num_to_pick += 1


        if K > 0:
            num_swaps = "IMPOSSIBLE"

        print "Case #%s: %s" % (case, num_swaps)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

