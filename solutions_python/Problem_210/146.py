#!/usr/bin/env python

import math
import networkx as nx
import numpy as np
import os
import sys
import time
from multiprocessing import Pool

sys.setrecursionlimit(100000)

NUM_PROCESSES = 12


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = end - start

    def __repr__(self):
        return 'Interval(start={0},end={1},duration={2})'.format(self.start, self.end, self.duration)

def is_interval_pair_half_day_apart(earlier, later):
    return abs(later.end - earlier.start) > 720 and abs(earlier.end - later.start) < 720


def small_solution(a_intervals, b_intervals):
    if len(a_intervals) == 2:
        if is_interval_pair_half_day_apart(a_intervals[0], a_intervals[1]):
            return 4
    elif len(b_intervals) == 2:
        if is_interval_pair_half_day_apart(b_intervals[0], b_intervals[1]):
            return 4
    return 2


def solution(spec):
    min_switches = small_solution(spec.a_intervals, spec.b_intervals)
    print 'Completed {0}'.format(spec.idx)
    return min_switches


class Spec(object):
    def __init__(self, idx, a_intervals, b_intervals):
        self.idx = idx
        self.a_intervals = sorted(a_intervals, key=lambda interval: interval.start)
        self.b_intervals = sorted(b_intervals, key=lambda interval: interval.start)


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
            num_a, num_b = [int(s) for s in first_line.split()]
            a_intervals = []
            for _ in xrange(num_a):
                values = [int(s) for s in in_f.readline().split()]
                a_intervals.append(Interval(values[0], values[1]))
            b_intervals = []
            for _ in xrange(num_b):
                values = [int(s) for s in in_f.readline().split()]
                b_intervals.append(Interval(values[0], values[1]))
            specs.append(Spec(idx, a_intervals, b_intervals))
            print '{0} initialized'.format(idx)
        # p = Pool(processes=NUM_PROCESSES)
        # results = p.map(solution, specs)
        results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}: {1}'.format(idx + 1, str(r))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()