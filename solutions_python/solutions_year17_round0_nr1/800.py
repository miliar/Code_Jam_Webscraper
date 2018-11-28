#!/usr/bin/python

import sys

def get_flips(S,K):
    flips = 0
    for i in range(len(S)-(K-1)):
        if S[i] != '+':
            S[i] = '+'
            flips += 1
            for j in range(i+1,i+K):
                if(S[j] == '+'):
                    S[j] = '-'
                else:
                    S[j] = '+'
    if '-' in ''.join(S):
        return 'IMPOSSIBLE'
    return flips


with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        S,K = f.readline().split()
        S=list(S)
        K = int(K)
        ans = get_flips(S,K)
        print("Case #{:}: {:}".format(case+1,ans)) 

