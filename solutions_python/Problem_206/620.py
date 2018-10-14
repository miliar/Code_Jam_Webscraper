#!/usr/bin/env python

import math
import os
import sys
import time
from multiprocessing import Pool

NUM_PROCESSES = 12


def solution(spec):
    horses = [Horse(h[0], h[1], spec.dest) for h in spec.horses]
    time_till_destinations = [h.ideal_time_till_destination for h in horses]
    max_time = max(time_till_destinations)
    return float(spec.dest) / max_time


class Horse(object):
    def __init__(self, initial_pos, speed, final_pos):
        self.initial_pos = initial_pos
        self.speed = speed
        self.final_pos = final_pos
        self.ideal_time_till_destination = float(final_pos - initial_pos) / float(speed)

    def __repr__(self):
        return 'Horse({0}, {1})'.format(self.initial_pos, self.speed, self.final_pos)

    def __str__(self):
        return self.__repr__() + ' Time till dest: {0}'.format(self.ideal_time_till_destination)


class Spec(object):
    def __init__(self, idx, destination, horses):
        self.idx = idx
        self.dest = destination
        self.horses = horses


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
            destination, num_horses = [int(s) for s in first_line.split()]
            horses = []
            for _ in xrange(num_horses):
                horses.append([int(s) for s in in_f.readline().split()])
            specs.append(Spec(idx, destination, horses))
            print '{0} initialized'.format(idx)
        p = Pool(processes=NUM_PROCESSES)
        results = p.map(solution, specs)
        # results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}: {1}'.format(idx + 1, str(r))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()