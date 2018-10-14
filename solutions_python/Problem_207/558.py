#!/usr/bin/env python

import math
import os
import sys
import time
from collections import namedtuple
from multiprocessing import Pool

sys.setrecursionlimit(100000)

NUM_PROCESSES = 12

def next_idx(idx, _list):
    return (idx + 1) if idx + 1 < len(_list) else 0

def prev_idx(idx, _list):
    return (idx - 1) if idx - 1 >= 0 else (len(_list) - 1)

def color_mismatch(_list, idx, color):
    return _list[idx] is not  None and _list[idx] & color

def can_place(_list, idx, color):
    return (not color_mismatch(_list, prev_idx(idx, _list), color) and
            not color_mismatch(_list, next_idx(idx, _list), color))

def __generate_stable(_list, remaining, idx=0):
    if idx == len(_list):
        return _list
    for c, num in remaining.iteritems():
        if num == 0:
            continue
        if can_place(_list, idx, c):
            _list[idx] = c
            remaining[c] -= 1
            result = __generate_stable(_list, remaining, idx+1)
            if result:
                return result
            remaining[c] += 1
            _list[idx] = None
    return None


def generate_stable(unicorns):
    return __generate_stable([None] * sum(unicorns.values()), unicorns)


def number_of_reds(color_cnts):
    return color_cnts.r + color_cnts.v + color_cnts.o

def number_of_yellows(color_cnts):
    return color_cnts.y + color_cnts.o + color_cnts.g

def number_of_blues(color_cnts):
    return color_cnts.b + color_cnts.g + color_cnts.v

def cardinal_colors(color_cnts):
    return [[number_of_reds(color_cnts), 'R'],
            [number_of_yellows(color_cnts), 'Y'],
            [number_of_blues(color_cnts), 'B']]

def place_stable(unicorns, color_cnts):
    ryb_cnts = cardinal_colors(color_cnts)
    max_cnt = max(ryb_cnts, key=lambda c: c[0])
    if max_cnt[0] > sum(unicorns.values())/2:
        return None
    _list = [None] * sum(unicorns.values())
    for i in xrange(max_cnt[0]):
        _list[i * 2] = max_cnt[1]
    ryb_cnts.remove(max_cnt)
    max_cnt = max(ryb_cnts, key=lambda c: c[0])
    idx = len(_list)-1
    for i in xrange(max_cnt[0]):
        while _list[idx]:
            idx -= 1
        _list[idx] = max_cnt[1]
        idx -= 2
    ryb_cnts.remove(max_cnt)
    max_cnt = ryb_cnts[0]
    idx = 0
    for i in xrange(max_cnt[0]):
        while _list[idx]:
            idx += 1
        _list[idx] = max_cnt[1]
        idx += 2
    return _list

def solution(spec):
    unicorns = numbers_dict(spec.color_cnts)
    result = place_stable(unicorns, spec.color_cnts)
    print 'Completed {0}'.format(spec.idx)
    return ''.join(result) if result else 'IMPOSSIBLE'

ColorCounts = namedtuple('ColorCounts', 'r, o, y, g, b, v')

def numbers_list(color_cnts):
    numbers = [1] * color_cnts.r + \
        [3] * color_cnts.o + \
        [2] * color_cnts.y + \
        [6] * color_cnts.g + \
        [4] * color_cnts.b + \
        [5] * color_cnts.v
    return numbers

NUMBER_TO_COLOR_MAPPING = {1: 'R',
                           3: 'O',
                           2: 'Y',
                           6: 'G',
                           4: 'B',
                           5: 'V'}
def colors_list(numbers):
    colors = [NUMBER_TO_COLOR_MAPPING[n] for n in numbers]
    return colors

def numbers_dict(color_cnts):
    numbers = {1: color_cnts.r,
               3: color_cnts.o,
               2: color_cnts.y,
               6: color_cnts.g,
               4: color_cnts.b,
               5: color_cnts.v}
    return numbers

class Spec(object):
    def __init__(self, idx, color_cnts):
        self.idx = idx
        self.color_cnts = color_cnts


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
            n, r, o, y, g, b, v = [int(s) for s in first_line.split()]
            specs.append(Spec(idx, ColorCounts(r, o, y, g, b, v)))
            print '{0} initialized'.format(idx)
        # p = Pool(processes=NUM_PROCESSES)
        # results = p.map(solution, specs)
        results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}: {1}'.format(idx + 1, str(r))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()