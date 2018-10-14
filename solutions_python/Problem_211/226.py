
# import random
# import math

# import heapq
# from collections import deque, defaultdict
# from scipy.misc import comb #use comb(n,k,True)
# from itertools import izip
# from functool import partial

# import numpy as np
# import sympy
# import networkx as nx
# from networkx.algorithms import bipartite




def NextSmall(N, K, U, P, v):
    p = sorted(P)
    check = sum(P)+U
    if sum(p) + U >= N:
        return float(1)
    if N == 1:
        return P[0]+U
    else:
        for i in xrange(N-1):
            if U < (i+1)*(p[i+1]-p[i]):
                for j in range(i+1):
                    p[j]+= U/(i+1)
                break
            else:
                U -= (i+1)*(p[i+1]-p[i])
                for j in range(i+1):
                    p[j] = p[i+1]
            #print i, U, p
            #print i, check, sum(p)+U
        else:
            for j in range(N):
                p[j]+= U/N
    pro = 1
    #print p
    for pi in p:
        pro *= pi
    return pro


#input = open(r'sample.in')
input = open(r'C-small-1-attempt3.in.txt')
# input = open(r'C-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    N, K = (int(s) for s in input.readline().strip().split())
    U = float(input.readline().strip())
    ls = [float(x) for x in input.readline().strip().split()]
    sol += [NextSmall(N, K, U, ls, verbose)]
    #if not i% 10: print i + 1
    print 'Case: ', i+1, 'done'

tofile = True
if tofile:
    with open(r'./outputC.txt', 'w') as output:
    #with open(r'./outputCL.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    for s in sol:
        print s


