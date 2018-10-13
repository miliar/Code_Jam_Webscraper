import sys
#import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
#import scipy as sp
import itertools
from string import maketrans

DISPLAY_RESULTS = False

def solve(N):
    N.reverse()
    for i in range(1,len(N)):
        if DISPLAY_RESULTS:
            print("".join(map(str,N)))
        if N[i] > N[i-1]:
            N[i] = N[i] - 1
            N = [9]*i + [N[i]] + N[i+1:]
        if DISPLAY_RESULTS:
            print("->"+"".join(map(str,N)))

    N.reverse()
    return "".join(map(str,N)).lstrip("0")



def solveAll(input, output=sys.stdout, case=None):
    T = int(input.readline())
    for case in xrange(T):
        N = map(int,list(input.readline().strip()))

        result= "Case #%d: %s\n" % (case + 1, solve(N))
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