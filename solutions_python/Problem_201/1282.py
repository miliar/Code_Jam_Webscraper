#!/usr/bin/env python2

import logging
import math

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
log = logging.getLogger("default")

results = { }


def calculate(num_stalls, num_people):
    cached = results.get((num_stalls, num_people))
    if cached:
        return cached

    if num_people == 1:
        r = num_stalls / 2
        if num_stalls % 2 == 0:
            return r, r - 1

        else:
            return r, r

    p = int(math.pow(2, int(math.log(num_people, 2))))

    values = []
    for i in xrange(p/2, p):
        max, min = calculate(num_stalls, i)
        values.append(max)
        values.append(min)

    values.sort(reverse=True)

    for person in xrange(p, 2*p):
        r = values[(person % p)]
        r2 = r / 2
        if r % 2 == 0:
            results[(num_stalls, person)] = r2, r2 - 1

        else:
            results[(num_stalls, person)] = r2, r2

    return results[(num_stalls, num_people)]



n = int(raw_input())  # cases
log.debug("Test cases: %d" % n)

for i in xrange(1, n + 1):
    log.debug("Starting test case: %d" % i)
    num_stalls, num_people = [int(s) for s in raw_input().split(" ")]

    max, min = calculate(num_stalls, num_people)
    log.debug("Input: %d %d, output: %d %d" % (num_stalls, num_people, max, min))

    print("Case #{}: {} {}".format(i, max, min))
