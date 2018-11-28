#!/usr/bin/env python
import sys
import numpy as np


def get_result(N, K):
    if K == 1:
        if N%2==0:
            return [N/2, N/2-1]
        else:
            return [(N-1)/2, (N-1)/2]
    Nmax, Nmin = get_result(N,1)
    arrN = np.zeros(K+1)
    arrN[0] = Nmin
    arrN[-1] = Nmax
    for i in xrange(K-2):
        #print arrN, Nmax
        Nmax = arrN[-1]
        newNmax, newNmin = get_result(Nmax,1)
        #print newNmax, newNmin
        arrN[-1] = newNmax
        arrN[1+i] = newNmin
        arrN = np.sort(arrN)
    Nmax = arrN[-1]
    return get_result(Nmax, 1)

if __name__=='__main__':
    infile = sys.argv[1]
    fin = open(infile,mode='r')
    Ncase = int(fin.readline().rstrip())
    for i in xrange(Ncase):
        line = fin.readline().rstrip()
        N = int(line.split()[0])
        K = int(line.split()[1])
        result = get_result(N, K)
        print "Case #%d: %d %d" % (i+1, result[0], result[1])



