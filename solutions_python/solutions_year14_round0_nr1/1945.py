#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

T = input()

for t in xrange(T):
    r1 = input()
    sq1 = [set([int(x) for x in raw_input().split()]) for i in xrange(4)]

    r2 = input()
    sq2 = [set([int(x) for x in raw_input().split()]) for i in xrange(4)]

    ret = sq1[r1 - 1] & sq2[r2 - 1]

    if len(ret) == 1:
        print 'Case #{0}: {1}'.format(t + 1, ret.pop())
        continue
    if len(ret) == 0:
        print 'Case #{0}: {1}'.format(t + 1, 'Volunteer cheated!')
        continue
    if len(ret) > 1:
        print 'Case #{0}: {1}'.format(t + 1, 'Bad magician!')
        continue

    
    

