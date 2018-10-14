#!/usr/bin/env python

import copy
import math
import networkx as nx
import numpy as np
import operator
import os
import sys
import time
from multiprocessing import Pool

sys.setrecursionlimit(100000)

NUM_PROCESSES = 12

def small_solution(spec):
    probs = copy.copy(spec.initial_probs)
    total_prob = sum(probs) + spec.adtl_prob
    avg_prob = total_prob / spec.num_probs
    for i in xrange(spec.num_probs-1,-1,-1):
        if probs[i] > avg_prob:
            avg_prob = (avg_prob - (probs[i]-avg_prob) / i) if i else 0
            probs.pop()
        else:
            break
    idx = len(probs)
    new_probs = [avg_prob] * idx + spec.initial_probs[idx:]
    return spec.success_prob(new_probs)

def solution(spec):
    suc_prob = small_solution(spec)
    print 'Completed {0}'.format(spec.idx)
    return suc_prob


class Spec(object):
    def __init__(self, idx, num_probs, min_trues, adtl_prob, initial_probs):
        self.idx = idx
        self.num_probs = num_probs
        self.min_trues = min_trues
        self.adtl_prob = adtl_prob
        self.initial_probs = sorted(initial_probs)

    def success_prob(self, probs):
        if self.min_trues == self.num_probs:
            return reduce(operator.mul, probs, 1)
        else:
            return 0


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
            num_probs, min_trues = [int(s) for s in first_line.split()]
            adtl_prob = float(in_f.readline().strip())
            initial_probs = [float(s) for s in in_f.readline().split()]
            specs.append(Spec(idx, num_probs, min_trues, adtl_prob, initial_probs))
            print '{0} initialized'.format(idx)
        # p = Pool(processes=NUM_PROCESSES)
        # results = p.map(solution, specs)
        results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}: {1}'.format(idx + 1, str(r))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()