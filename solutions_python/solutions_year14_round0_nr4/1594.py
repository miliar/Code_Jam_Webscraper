#!/usr/bin/python

import sys

def readfloats(f):
    return [float(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [readints(f)]
    return matrix

def opt(my, ken):
    kenMin = -1;
    kenOpt = -1;
    for i in xrange(len(ken)):
        if kenMin < 0 or ken[kenMin] > ken[i]:
            kenMin = i
        if ken[i] > my and (kenOpt < 0 or ken[kenOpt] > ken[i]):
            kenOpt = i
    k = -1
    if kenOpt >= 0:
        k = ken.pop(kenOpt)
    else:
        k = ken.pop(kenMin)
    return k, ken

def dec(n, nao, ken):
    nao = nao[:]
    nao.sort()
    ken = ken[:]
    ken.sort()
    while len(nao) > 0:
        if all([nao[i] > ken[i] for i in xrange(len(nao))]):
            break
        nao.pop(0)
        ken.pop()
    return len(nao)
 
def sim(n, nao, ken):
    score = 0
    while len(nao) > 0:
        my = nao.pop()
        k, ken = opt(my, ken)
        if my > k:
            score += 1
    return score

def war(f):
    n = readint(f)
    nao = readfloats(f)
    ken = readfloats(f)

    return dec(n, nao, ken), sim(n, nao, ken)

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        d, w = war(f)
        print "Case #%d: %d %d" % (i + 1, d, w)
