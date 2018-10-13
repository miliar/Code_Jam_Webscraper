#!/usr/bin/env python

import sys
import ctypes
import logging

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(message)s')
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')


def strategy(S, K):
    logging.debug("  Got S:[{}] and K:[{}]".format(S, K))

    s = ctypes.create_string_buffer(S)
    flips = 0
    for i in range(len(s) - K + 1):
        slice = s[i:i + K]
        if (i + K) == len(s):
            continue
        logging.debug("    Decide on part [{}]".format(slice))
        if slice.startswith('+'):
            continue
        else:
            for j in range(i, i + K):
                s[j] = '+' if s[j] == '-' else '-'
            slice = s[i:i + K]
            logging.debug("      * Flipping to [{}]".format(slice))
            logging.debug("      * New state [{}]".format(s.value))
            flips += 1

    if '-' in s:
        flips = 'IMPOSSIBLE'
    return flips


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        S = line[0]
        K = int(line[1])
        logging.debug("Starting case #%s" % (i + 1))
        logging.info('Case #%s: %s' % (i + 1, strategy(S, K)))

main(sys.stdin)
