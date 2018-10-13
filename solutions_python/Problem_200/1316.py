#!/usr/bin/env python2

import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("default")

def tidyness(num):
    index = 0
    length = len(num)

    tidy = ""
    prev_digit = 0

    for current_char in num[::-1]:
        current_digit = int(current_char)
        if index > 0:
            if current_digit > prev_digit:
                current_digit -= 1

                # replace what we wrote so far with 9's
                tidy = "9"*index

            else:
                tidy += str(prev_digit)

        prev_digit = current_digit
        index += 1

    if prev_digit > 0:
        tidy += str(prev_digit)

    return tidy[::-1]


n = int(raw_input())  # cases
log.debug("Test cases: %d" % n)

for i in xrange(1, n + 1):
    log.debug("Starting test case: %d" % i)
    num = raw_input()

    tidy = tidyness(num)
    log.debug("Input: %s, output: %s" % (num, tidy))

    print("Case #{}: {}".format(i, tidy))
