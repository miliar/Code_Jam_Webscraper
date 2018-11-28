#!/usr/bin/env python2

import logging
import itertools
import math

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
log = logging.getLogger("default")

class Pancake(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

def calculate(n, k, pancakes):
    #pancakes.sort(key=lambda p: p.radius)
    max_area = 0.0
    for c in itertools.combinations(range(n), k):
        stack = [pancakes[i] for i in c]

        # sort by radius
        stack.sort(key=lambda p: p.radius, reverse=False)

        area = 0.0
        last_radius = 0

        for pancake in stack:
            # add the sides  2*pie*R*H
            area += math.pi * 2 * pancake.radius * pancake.height

            # calculate top  pi*r^2 - previous
            rd = pancake.radius*pancake.radius - last_radius*last_radius
            area += math.pi * rd
            last_radius = pancake.radius

        if area > max_area:
            max_area = area

    return max_area



t = int(raw_input())  # cases


log.debug("Test cases: %d" % t)

for i in xrange(1, t + 1):
    log.debug("Starting test case: %d" % i)
    n, k = [int(z) for z in raw_input().split(" ")]

    radii = []
    heights = []
    pancakes = []

    for j in xrange(1, n + 1):
        r, h = [int(z) for z in raw_input().split(" ")]
        pancakes.append(Pancake(r, h))
        #radii.append(r)
        #heights.append(h)

    r = calculate(n, k, pancakes)
    #log.debug("Input: %s %d, output: %s" % (s, k, m))

    print("Case #{}: {}".format(i, r))
