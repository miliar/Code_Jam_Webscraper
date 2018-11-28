

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




def Next(N, R, O, Y, G, B, v):
    return 1

def NextSmall(N, R, Y, B, v):
    colors = sorted([(R, 'R'), (Y, 'Y'), (B, 'B')], reverse = True)
    Z, Y, X = (c[0] for c in colors)
    red, blue, green = (c[1] for c in colors)
    if Z > Y + X:
        return 'IMPOSSIBLE'
    else:
        E = X + Y -Z
        stable1 = ''.join(red +blue for i in xrange(Y-E))
        stable2 = ''.join(red+blue+green for i in xrange(E))
        stable3 = ''.join(red+green for i in xrange(X - E))
        return stable1+stable2+stable3



    
#input = open(r'sample.in')
input = open(r'B-small-attempt0.in.txt')
#input = open(r'B-largein.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    N, R, O, Y, G, B, V = (int(s) for s in input.readline().strip().split())
    ls = []
    sol += [NextSmall(N, R, Y, B, verbose)]
    if not i%10: print i+1
    #print 'Case: ', i+1, 'done'


tofile = True
if tofile:
    with open(r'./outputB.txt', 'w') as output:
    #with open(r'./outputBL.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    for s in sol:
        print s


