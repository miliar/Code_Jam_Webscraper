import glob, pprint, pickle, os, time, sys
from copy import copy
from zope.interface.tests import odd
from numpy import array, sin, cos
import numpy as np
import itertools
import math
import itertools
import random
from collections import defaultdict




def solve(horses, distance_grid, post, totaltime = 0):

    current_horse_speed = horses[0][1]
    current_horse_dist = horses[0][0]


    # we travel to next city
    dst = distance_grid[0][1]
    current_horse_dist -= dst
    if current_horse_dist < 0:
        return float('inf')
    totaltime += 1. * dst/current_horse_speed

    if len(horses)==2:
        return totaltime

    # do we switch horses?


    # try all possibilities recursively
    # 1) assume we switch horses
    ndist = [dist[1:] for dist in distance_grid[1:]]
    nhorses = horses[1:]
    res_A = solve(nhorses, ndist, post, totaltime)

    # 2) assume we keep horses
    if current_horse_dist>nhorses[0][0] or current_horse_speed>nhorses[0][1]:
        nhorses[0] = [current_horse_dist, current_horse_speed]
        res_B = solve(nhorses, ndist, post, totaltime)
        res = min(res_A, res_B)

    return res

output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    def read_frac():
        return [int(x) for x in f.readline().strip().split('/')]
    def read_strs():
        return [x for x in f.readline().strip().split(' ')]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        N,Q = read_ints()
        horses = []
        for n in xrange(N):
            horses.append(read_ints())

        distance_grid = []
        for n in xrange(N):
            distance_grid.append(read_ints())

        post = []
        for q in xrange(Q):
            post.append(read_ints())


        answer = solve(horses, distance_grid, post)

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()