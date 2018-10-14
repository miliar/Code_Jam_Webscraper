infilecode = "CS0I"

import sys
#from copy import deepcopy
from math import ceil, floor
#import networkx as nx
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())

for case in range(1,T+1):
    
    Hd, Ad, Hk, Ak, B, D = map(int,input().split())
    
    print(Hd, Ad, Hk, Ak, B, D)

    attacks = 100
    for numbuffs in range(101):
        attack = Ad + numbuffs * B
        turns = numbuffs + ceil(Hk / attack)
        attacks = min(attacks, turns)
    print("attacks =", attacks)

    answer = 1000
    if D == 0:
        maxdebuffs = 0
    else:
        maxdebuffs = ceil(Ak / D)
    for debuffs in range(maxdebuffs+1):
        #print("debuffs=",debuffs)
        H = Hd
        A = Ak
        N = attacks
        Nd = debuffs
        #print(H,A,N,Nd)
        bag = set()
        while (H,A,N,Nd) not in bag and N>0 and H>0:
            bag |= {(H,A,N,Nd)}
            if N == 1:
                N -= 1
            elif (Nd == 0 and A >= H) or (Nd > 0 and A-D >= H):
                H = Hd
            elif Nd > 0:
                Nd -= 1
                A -= D
            else:
                N -= 1

            if N > 0:
                H -= A

            #print(H,A,N,Nd)
        #print(len(bag))
        if N > 0 or H<=0:
            turns = 1000
        else:
            turns = len(bag)
        answer = min(answer,turns)





    if answer == 1000:
        answer = "IMPOSSIBLE"


    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
