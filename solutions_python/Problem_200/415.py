import glob, pprint, pickle, os, time, sys
from copy import copy
import heapq
from numpy import array, sin, cos, zeros
import itertools
import math
import numpy as np
import bisect


def int_to_list(N):
    return map(int, str(N))

def list_to_int(l):
    return int(''.join( map(str, l)))

def solve(N):
    good = False
    while not good:
        good = True
        Nl = int_to_list(N)
        for i in xrange(len(Nl)-1):
            if Nl[i]>Nl[i+1]:
                # find the best fix:
                N -= 1 + list_to_int(Nl[i+1:])
                good = False
                break
    return N



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
    def read_cakes():
        return [True if x=='+' else False for x in f.readline().strip()]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        N, = read_ints()
        answer = solve(N)

        ### output ###
        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()