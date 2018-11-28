import sys
#import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
#import scipy as sp
import itertools
from string import maketrans

DISPLAY_RESULTS = False

def solve(N,K):
    spaces = {N:1}
    while K:
        best_space = max(spaces.keys())
        L = best_space / 2
        R = best_space - L - 1
        used_spaces = min(K, spaces[best_space])
        spaces[best_space]-=used_spaces
        if spaces[best_space] == 0:
            del spaces[best_space]
        if L not in spaces:
            spaces[L]=0
        if R not in spaces:
            spaces[R]=0
        spaces[L]+=used_spaces
        spaces[R]+=used_spaces
        K -= used_spaces
        if DISPLAY_RESULTS:
            print spaces

    return "{} {}".format(L,R)



def solveAll(input, output=sys.stdout, case=None):
    T = int(input.readline())
    for case in xrange(T):
        N,K = map(int,list(input.readline().strip().split(' ')))

        result= "Case #%d: %s\n" % (case + 1, solve(N,K))
        output.write(result)
        if output != sys.stdout:
            sys.stdout.write(result)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        in_fd = open(sys.argv[1])
        out_fd = open(sys.argv[1].replace('input','output'),'w')
        solveAll(in_fd, out_fd)
        out_fd.close()
        in_fd.close()
    else:
        solveAll(sys.stdin)