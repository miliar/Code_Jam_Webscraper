

#import random
#import math

#import heapq
#from collections import deque, defaultdict
#from scipy.misc import comb #use comb(n,k,True)
#from itertools import izip
#from functool import partial

#import numpy as np
#import sympy
#import networkx as nx
#from networkx.algorithms import bipartite




def Next(D, N, KS, v):
    slow = max((D-s[0])/s[1] for s in KS)
    ans = D/slow
    return str(str(ans))

    
#input = open(r'sample.in')
#input = open(r'A-small-attempt0.in.txt')
input = open(r'A-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    D, N = (int(s) for s in input.readline().strip().split())
    KS = []
    for j in xrange(N):
        b, c = input.readline().strip().split()
        KS.append((float(b), float(c)))
    sol += [Next(D, N, KS, verbose)]
    if not i%10: print i+1
    #print 'Case: ', i+1, 'done'


tofile = True
if tofile:
    with open(r'./outputAL.txt', 'w') as output:
    #with open(r'./outputAL.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    for s in sol:
        print s


