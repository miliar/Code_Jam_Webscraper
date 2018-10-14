#!/usr/bin/env python

from __future__ import division, print_function
import math
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))

        depth = int(math.log(K) / math.log(2))
        level_size = 2**depth
        level_nodes = N - (level_size - 1)
        level_used_nodes = K - (level_size - 1)

        if level_used_nodes <= level_nodes % level_size:
            distance = math.ceil(level_nodes / level_size)
        else:
            distance = math.floor(level_nodes / level_size)

        if distance > 1:
            distance = (distance - 1) / 2
            print('Case #%d:' % (i + 1), math.ceil(distance), math.floor(distance))
        else:
            print('Case #%d: 0 0' % (i + 1))
