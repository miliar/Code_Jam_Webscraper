#!python2
from __future__ import division, print_function

import sys
from pprint import pprint as pp
import math as m
from itertools import count

def dwar(A, B):
    pt = 0
    i = 0  # index in B
    for a in A:
        b = B[i]
        if a > b:
            i += 1
            pt += 1
    return pt

def war(A, B):
    pt = len(A)
    i = 0  # index in A
    for b in B:
        a = A[i]
        if b > a:
            i += 1
            pt -= 1
    return pt

def result(N, A, B): # A is Naomi, B is Ken
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    return '{} {}'.format(dwar(A, B), war(A, B))

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N = float(sys.stdin.readline().strip())
        A = [float(s.strip()) for s in
             sys.stdin.readline().strip().split()]
        B = [float(s.strip()) for s in
             sys.stdin.readline().strip().split()]
        #if t+1 != 49: continue
        print("Case #{}: {}".format(str(t+1), result(N, A, B)))
