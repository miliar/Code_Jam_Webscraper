#!/usr/bin/env python3

from math import *

def pick(P,K):
    Smax = 0
    for i in range(K-1,len(P)):
        H = [h for (_,h) in P[:i]]
        assert(len(H)>=K-1)
        H.sort(reverse=True)
        assert(len(H[:K-1])==K-1)
        S = P[i][0]+P[i][1]+sum(H[:K-1])
        Smax = max(Smax,S)
    return Smax

def main():
    T = int(input())
    for t in range(1,T+1):
        N,K = map(int,input().split())
        P = []
        for _ in range(N):
            Ri,Hi = map(int,input().split())
            P.append((pi*Ri*Ri,2*pi*Ri*Hi))
        P.sort()
        print('Case #%d: %.9f' % (t,pick(P,K)))

main()
