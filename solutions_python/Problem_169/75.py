import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos, zeros
import itertools
import math
import numpy as np

def solve1(r,c,v,x):
    if x==c:
        return v/r,
    else:
        return "IMPOSSIBLE",

def solve2(v,x,r1,c1,r2,c2):
    if x>max(c1,c2) or x<min(c1,c2):
        return "IMPOSSIBLE",



    matr = np.array([[r1,r2],[r1*c1-r1*x, r2*c2-r2*x]])
    if np.linalg.det(matr)==0:
        assert c1==c2
        return solve1(r1+r2,c1,v,x)

    res = np.array([v,0]).T

    result = np.dot(np.linalg.inv(matr),res)

    return np.max(result),

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
        N,v,x = read_floats()
        N = int(N)
        if N==1:
            r,c = read_floats()
            answer = solve1(r,c,v,x)

        elif N==2:
            r1,c1 = read_floats()
            r2,c2 = read_floats()
            answer = solve2(v,x,r1,c1,r2,c2)


        ### output ###
        if isinstance(answer[0],float):
            answer_str = "Case #{}: {:.10f}".format(questionindex+1, answer[0])
        else:
            answer_str = "Case #{}: {}".format(questionindex+1, answer[0])
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()