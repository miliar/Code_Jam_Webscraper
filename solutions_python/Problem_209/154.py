#!/usr/bin/env python

import copy
import math
import networkx as nx
import numpy as np
import os
import sys
import time
from multiprocessing import Pool

sys.setrecursionlimit(100000)

NUM_PROCESSES = 12

class Pancake(object):
    def __init__(self, radius, height):
        self.r = radius
        self.h = height
        self.top_area = math.pi * math.pow(self.r, 2)
        self.height_area = 2 * math.pi * self.r * self.h

    def __repr__(self):
        return 'Pancake: r:{0}, h:{1} (top:{2}, height:{3})'.format(self.r, self.h, self.top_area, self.height_area)


def maximum_area(stack_height, pancakes):
    current_max = [pancakes[i].top_area + pancakes[i].height_area for i in xrange(len(pancakes))]
    for i in xrange(1,stack_height):
        new_current_max = copy.copy(current_max)
        for j in xrange(i,len(pancakes)):
            new_current_max[j] = max([current_max[k]+pancakes[j].height_area for k in xrange(j)])
        current_max = new_current_max
    return max(current_max)


def solution(spec):
    max_area = maximum_area(spec.stack_height,
                            sorted(spec.pancakes, key=lambda p:p.r, reverse=True))
    print 'Completed {0}'.format(spec.idx)
    return max_area


class Spec(object):
    def __init__(self, idx, stack_height, pancakes):
        self.idx = idx
        self.stack_height = stack_height
        self.pancakes = pancakes


class Stopwatch(object):
    def __init__(self):
        self.start_ts = time.time()

    def end_and_print(self):
        print '{0}s'.format(time.time() - self.start_ts)


if __name__ == '__main__':
    stopwatch = Stopwatch()
    in_filename = sys.argv[1]
    out_filename = os.path.splitext(in_filename)[0] + '.out'
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        num_tests = int(in_f.readline())
        specs = []
        for idx in xrange(num_tests):
            first_line = in_f.readline()
            num_pancakes, num_stack = [int(s) for s in first_line.split()]
            pancakes = []
            for _ in xrange(num_pancakes):
                values = [float(s) for s in in_f.readline().split()]
                pancakes.append(Pancake(values[0], values[1]))
            specs.append(Spec(idx, num_stack, pancakes))
            print '{0} initialized'.format(idx)
        p = Pool(processes=NUM_PROCESSES)
        results = p.map(solution, specs)
        #results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}: {1}'.format(idx + 1, str(r))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()