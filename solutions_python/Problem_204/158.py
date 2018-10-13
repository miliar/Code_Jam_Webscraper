infilecode = "BS1I"

import sys
from copy import deepcopy
import math
#import networkx as nx
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())

for case in range(1,T+1):
    
    N, P = map(int,input().split())
    R = list(map(int,input().split()))
    Q = []
    for i in range(N):
        Q1 = sorted(list(map(int,input().split())))
        print(Q1)
        Q += [Q1]

    #print(N,P,R,Q)


    low = deepcopy(Q)
    high = deepcopy(Q)
    span = [ [] for i in range(N) ]

    for i in range(N):
        a = R[i]
        bb = (a*0.9)
        cc = (a*1.1)
        for j in range(P):
            high[i][j] = math.floor(Q[i][j] / bb)
            low[i][j] = math.ceil(Q[i][j] / cc)
            if low[i][j] <= high[i][j]:
                span[i] += [(math.ceil(Q[i][j] / cc), math.floor(Q[i][j] / bb))]

    print(span)

    answer = 0

    while min( len(xx) for xx in span) > 0:
        lo = 1
        hi = 1000000

        lo = max( span[i][0][0] for i in range(N))
        hi = min( span[i][0][1] for i in range(N))
        if lo <= hi:
            answer += 1
            for i in range(N):
                span[i] = span[i][1:]
        else:
            for i in range(N):
                if span[i][0][1] < lo:
                   span[i] = span[i][1:]


            







    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
