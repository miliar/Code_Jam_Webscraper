import sys
import numpy as np

def flip(S, idx):
    if S[idx] == '-':
        S[idx] = '+'
    elif S[idx] == '+':
        S[idx] = '-'

def run_flips(idx, K, S):
    for subidx in range(idx, idx+K):
        if subidx >= len(S):
            return False
        flip(S, subidx)
    return True

def greedy(Sin, K):
    S = list(Sin)
    flips = 0
    for idx, s in enumerate(S):
        #print("greedy", idx, S)
        if s == '-':
            flips += 1
            if not run_flips(idx, K, S):
                return "IMPOSSIBLE"
    return str(flips)

def all_pluses(S):
    for s in S:
        if s == '-':
            return False
    return True

def brute(Sin, K):
    minflips = len(Sin)+1
    for sol in range((1 << (len(Sin)-K+1))):
        #print("sol=", sol)
        #evaluate curr sol
        S = list(Sin)
        currflips = 0
        for i in range(len(S)-K+1):
            #print("i=", i)
            if (1 << i) & sol:
                currflips += 1
                if not run_flips(i, K, S):
                    print("ERROR in brute!")
            #print("S=", S)
        if all_pluses(S):
            minflips = min(minflips, currflips)
        #print("minflips=", minflips)
    
    if minflips == len(Sin)+1:
        return "IMPOSSIBLE"
    return str(minflips)

T=int(sys.stdin.readline())
for t in range(1, T+1):
    line=sys.stdin.readline()
    [S, K]=line.split()
    K = int(K)
    #print(S, K)
    
    res = greedy(S, K)
    print "Case #"+str(t)+": "+res
    #res = brute(S, K) 
    #print "Case #"+str(t)+": "+res
