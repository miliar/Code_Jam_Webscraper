#!/usr/bin/env python

import logging

#INPUT_FILENAME = "A-test.in"
#INPUT_FILENAME = "A-small-attempt0.in"
INPUT_FILENAME = "A-large.in"

def main():
    for case, line in enumerate(file(INPUT_FILENAME)):
        if case == 0:
            continue
        N, K = [int(v) for v in line.split()]
        chain = 2**N - 1
        result = (K & chain) == chain

        result = "ON" if result else "OFF"
        print "Case #%s: %s" % (case, result)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

