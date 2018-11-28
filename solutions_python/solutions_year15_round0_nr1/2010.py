#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    sample = sys.stdin.readline()
    max_s, audience = sample.strip().split(' ')
    max_s = int(max_s)
    friends = 0
    standing = 0
    for shyness, members in enumerate(audience):
        if shyness - (standing + friends) > 0:
            friends += (shyness - (standing + friends))
        standing += int(members)
    print 'Case #%d: %d'%(i+1, friends)
