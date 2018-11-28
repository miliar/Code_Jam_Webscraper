#!/usr/bin/env python2

import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
log = logging.getLogger("default")


def count_flips(s, k):
    length = len(s)
    flips = 0

    bits = []
    for ch in s:
        if ch == "+":
            bits.append(True)

        else:
            bits.append(False)

    for index in xrange(0, length-k+1):
        if bits[index] == False:
            flips += 1

            for j in xrange(index, index+k):
                bits[j] = not bits[j]

        index +=1

    for i in xrange(length-k, length):
        if not bits[i]:
            return "IMPOSSIBLE"

    return flips


n = int(raw_input())  # cases
log.debug("Test cases: %d" % n)

for i in xrange(1, n + 1):
    log.debug("Starting test case: %d" % i)
    s, k = [t for t in raw_input().split(" ")]
    k = int(k)

    m = count_flips(s, k)
    log.debug("Input: %s %d, output: %s" % (s, k, ""))

    print("Case #{}: {}".format(i, m))