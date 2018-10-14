#!/usr/bin/python
# Python 2.6

import sys
from util import FileReader

#import re
#import itertools
#from collections import defaultdict


def main():

    if len(sys.argv) < 2:
        print "usage: {0} <input-file>".format(__file__)
        sys.exit(-1)

    with open(sys.argv[1]) as _file:
        file = FileReader(_file)

        T = file.int()
        for t in xrange(T):

            input = file.string()

            digits = set(input)

            orders = []
            for d in digits:
                orders.append((input.index(d), d))

            orders.sort()

            values = {}
            value = 0
            for i, c in orders:
                values[c] = value
                value += 1

            base = len(orders)

            if base == 1:
                values[orders[0][1]] = 1
                base = 2

            else:
                values[orders[0][1]] = 1
                values[orders[1][1]] = 0

            result = 0
            pow = 0
            for c in reversed(input):
                result += values[c] * (base ** pow)
                pow += 1

            print "Case #{0}: {1}".format(t+1, result)


if __name__ == "__main__":
    main()

