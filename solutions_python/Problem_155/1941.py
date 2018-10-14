#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.stdin.readline()

def verify(line, result):
    hall = [0] * result
    for i, c in enumerate(line):
        hall += [i] * int(c)
    for i, s in enumerate(hall):
        if s > i:
            print  >>sys.stderr, line, result
            raise RuntimeError, "{} {}".format(i, hall)

for case, line in enumerate(sys.stdin,1):
    fields = line.strip().split()
    smax = int(fields[0])
    persons = fields[1]
    standing = 0
    required = 0
    # 0200202
    for shyness in xrange(smax + 1):
        cur = int(persons[shyness])
        if cur > 0 and shyness > standing:
            required += shyness - standing
            standing += shyness - standing
        standing += cur
    verify(fields[1], required)
    print "Case #{case}: {required}".format(case=case, required=required)
        
    


