# python2
import sys
import math
import random
import heapq
from bintrees import AVLTree
import itertools


def A():
    return True


class main():
    T = int(sys.stdin.readline().rstrip())
    
    for t in range(T):
        line = sys.stdin.readline().rstrip()
        S = line.split()
        D = int(S[0])
        N = int(S[1])

        maxi = -1.0
        for i in range(N):
            line = sys.stdin.readline().rstrip()
            S = line.split()
            K = float(S[0])
            S = float(S[1])
            if (maxi < (D-K)/S):
                maxi = (D-K) / S
        
        print "Case #" + str(t+1) + ": " + str(D/maxi)
