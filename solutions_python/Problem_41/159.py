#!/usr/bin/env python

import sys
import math

def digit_distribution(number):
    buckets = {}

    for i in range(1, 10):
        buckets[i] = 0

    while number > 0:
        place_value = number%10
        if place_value > 0:
            if place_value not in buckets:
                buckets[place_value] = 1
            else:
                buckets[place_value] += 1
        number /= 10
    return buckets

def distribution_valid(base, current):
    for digit, value in base.items():
        if(digit not in current or value != current[digit]):
            return False
    return True

def dump_distribution(buckets):
    for digit in range(1, 10):
        print >> sys.stderr, buckets[digit]


def digit_match(number):
    buckets = digit_distribution(number)
    #dump_distribution(buckets)
    num = number + 1
    while not distribution_valid(buckets, digit_distribution(num)):
        num = num + 1
    return num

firstline = True
count = 1
for line in sys.stdin:
    if firstline:
        firstline = False
    else:
        print >> sys.stderr, "working on %s" % line.strip()
        print "Case #%d: %d" % (count, digit_match(int(line.strip())))
        count += 1

