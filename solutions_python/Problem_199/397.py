import glob, pprint, pickle, os, time, sys
from copy import copy
from operator import itemgetter
from numpy import array, sin, cos
import numpy as np
import itertools
import math

BIGINT = 10**128
import sys
sys.setrecursionlimit(10000)


def solve(s,K):
    if isinstance(s,str):
        s = [True if i=='+' else False for i in s]
    N = len(s)
    res = 0
    if not s[0]:
        res += 1
        for i in xrange(K):
            s[i] = not s[i]

    if len(s)==K:
        good = True
        for i in xrange(K):
            if not s[i]:
                good = False
                break
        if good:
            return res
        return float('NaN')
    res += solve(s[1:],K)
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
    def read_chrs():
        return [x for x in f.readline().strip()]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        s,K = read_strs()
        answer = solve(s,int(K))
        if answer != answer: # test if NaN
            answer= "IMPOSSIBLE"

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()