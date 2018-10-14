#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys

lines = [[int(y) for y in x.split()] for x in sys.stdin.readlines()]

index = 1
for line in lines[2::2]:
    ret = 0
    for i in range(len(line)):
        if line[i] != i + 1:
            ret += 1.0
    print "Case #%d: %.6f" % (index, ret)
    index += 1

