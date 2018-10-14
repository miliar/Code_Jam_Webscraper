
# import random
import math

# import heapq
# from collections import deque, defaultdict
# from scipy.misc import comb #use comb(n,k,True)
# from itertools import izip
# from functool import partial

# import numpy as np
# import sympy
# import networkx as nx
# from networkx.algorithms import bipartite




def Next(N, K, ps, v):
    pside = sorted(ps, reverse=True)
    take = pside[:K-1]
    if K > 1:
        ptop = max(take, key=lambda pan: pan[1])
    else:
        ptop = [0,0]
    e = 0
    for i in range(K-1, N):
        #print pside, ptop
        extra = 2*pside[i][0] + max(pside[i][1]**2-ptop[1]**2, 0)
        if extra > e:
            e = extra
    area = ptop[1]**2 + 2*sum(t[0] for t in take) + e
    return str(math.pi *area)


#input = open(r'sample.in')
#input = open(r'A-small-attempt0.in.txt')
input = open(r'A-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    N,K = (int(s) for s in input.readline().strip().split())
    ls = []
    for j in xrange(N):
        R, H = input.readline().strip().split()
        ls.append([int(R)*int(H), int(R), int(H)])
    sol += [Next(N, K, ls, verbose)]
    #if not i% 10: print i + 1
    print 'Case: ', i+1, 'done'


tofile = True
if tofile:
    with open(r'./outputA.txt', 'w') as output:
    #with open(r'./outputAL.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    for s in sol:
        print s


