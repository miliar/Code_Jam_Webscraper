import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos
import numpy as np
import itertools
import math

def checktoright(g,i,j):
    for k in xrange(j+1,g.shape[1]):
        if g[i][k]!=0:
            return True
    return False

def checktoleft(g,i,j):
    for k in xrange(j-1,-1,-1):
        if g[i][k]!=0:
            return True
    return False

def checktoup(g,i,j):
    for k in xrange(i-1,-1,-1):
        if g[k][j]!=0:
            return True
    return False

def checktodown(g,i,j):
    for k in xrange(i+1,g.shape[0]):
        if g[k][j]!=0:
            return True
    return False

def solve(g):
    mmap = {62:1, 118:2, 60:3, 94:4, 46:0}
    for i in xrange(g.shape[0]):
        for j in xrange(g.shape[1]):
            g[i,j] = mmap[g[i,j]]

    total = 0
    for i in xrange(g.shape[0]):
        for j in xrange(g.shape[1]):
            if g[i][j]==0:
                continue
            elif g[i][j]==1:
                if not checktoright(g,i,j):
                    if checktoleft(g,i,j) or checktodown(g,i,j) or checktoup(g,i,j):
                        total += 1
                    else:
                        return "IMPOSSIBLE",
            elif g[i][j]==2:
                if not checktodown(g,i,j):
                    if checktoleft(g,i,j) or checktoright(g,i,j) or checktoup(g,i,j):
                        total += 1
                    else:
                        return "IMPOSSIBLE",
            elif g[i][j]==3:
                if not checktoleft(g,i,j):
                    if checktodown(g,i,j) or checktoright(g,i,j) or checktoup(g,i,j):
                        total += 1
                    else:
                        return "IMPOSSIBLE",
            elif g[i][j]==4:
                if not checktoup(g,i,j):
                    if checktodown(g,i,j) or checktoright(g,i,j) or checktoleft(g,i,j):
                        total += 1
                    else:
                        return "IMPOSSIBLE",
    return total,

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
        (r,c) = read_ints()
        g = np.zeros((r,c),dtype='int32')
        for i in xrange(r):
            #print read_chrs()
            g[i,:] = [ord(c) for c in read_chrs()]
        answer = solve(g)

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]))
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()