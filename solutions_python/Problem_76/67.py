#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys

lines = [[int(y) for y in x.split()] for x in sys.stdin.readlines()]

def patsum(args):
    return reduce(lambda x, y: (x | y) ^ (x & y), args)

index = 1
for line in lines[2::2]:
    if patsum(line) == 0:
        print "Case #%d: %d" % (index, sum(line) - min(line))
    else:
        print "Case #%d: NO" % index
    index += 1

