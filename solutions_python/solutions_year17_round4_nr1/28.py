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


def solve(N,P,G):
    if P==2:
        even = len([g for g in G if g%2==0])
        odd =  len([g for g in G if g%2==1])
        return even+(odd+1)/2

    if P==3:
        off0 = len([g for g in G if g%P==0])
        off1 = len([g for g in G if g%P==1])
        off2 =  len([g for g in G if g%P==2])

        off1off2combo = min(off1, off2)

        off1 -= off1off2combo
        off2 -= off1off2combo

        return off0 + off1off2combo + (off1+2)/3  + (off2+2)/3


    if P==4:
        off0 = len([g for g in G if g%P==0])
        off1 = len([g for g in G if g%P==1])
        off2 =  len([g for g in G if g%P==2])
        off3 =  len([g for g in G if g%P==3])

        off2off2combo = min(off1, off2)

        off2 -= off1off2combo

        return off0 + off1off2combo + (off1+2)/3  + (off2+2)/3


    return 0


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
        N,P = read_ints()
        G = read_ints()


        answer = solve(N,P,G)

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()