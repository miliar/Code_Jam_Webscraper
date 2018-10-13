#!/usr/bin/env python

import sys
import ctypes
import logging

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(message)s')
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')


def strategy(N):
    logging.debug("  Got N:[{}]".format(N))
    if N < 10:
        return N

    strN = ctypes.create_string_buffer(str(N))
    while True:
        flag = True
        for i in range(len(strN) - 2):
            if strN[i] > strN[i + 1]:
                reason = ("{} > {}".format(strN[i], strN[i + 1]))
                strN[i] = str(int(strN[i]) - 1)
                for j in range(i + 1, len(strN) - 1):
                    strN[j] = '9'
                logging.debug("    Converted to [{}] because [{}]".format(strN.value, reason))
                flag = False
            else:
                logging.debug("    Keeped    to [{}] because [{} <= {}]".format(strN.value, strN[i], strN[i + 1]))
        if flag:
            break

    return int(strN.value)


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        N = int(line[0])
        logging.debug("Starting case #%s" % (i + 1))
        logging.info('Case #%s: %s' % (i + 1, strategy(N)))

main(sys.stdin)
