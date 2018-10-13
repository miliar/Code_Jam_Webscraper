#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:15:08 2017

@author: shuzheng
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:54:02 2017

@author: shuzheng
"""

def findallneg(S, K):
    #remove the last one that inside K mostright side
    S_n = list(S)
    index = []
    i = 0
    for sn in S_n:
        if i >len(S)-K:
            i = i + 1
            continue
        if sn=='-':
            index.append(i)
        i = i + 1
    return index

def flipchar(s):
    if s=='+':
        return '-'
    if s=='-':
        return '+'

def flipsubset(S, K, index):
    S_n = list(S)
    for i in range(0,K):
        S_n[index[0]+i] = flipchar(S_n[index[0]+i])
    return "".join(S_n)


def checkifok(S):
    if s == len(s) * s[0]:
        if s[0] == '+':
            return True
        if s[0] == '-':
            return False

def checkifcontains(S):
    if '-' not in S:
        return True
    else:
        return False

def reverse_part(S,K):
    count = 0
    while(not checkifok(S)):
        index_neg = findallneg(S, K)
        #print index_neg
        if not index_neg:
            break
        S = flipsubset(S, K, index_neg)
        count = count + 1
    if not checkifcontains(S):
        return "IMPOSSIBLE"
    else:
        return count
    
def solve(n,m):
    S = n
    K = int(m)
    length_S = len(S)
    
    
    if S == len(S) * S[0]:
        if s[0] == '+':
            return 0
        if s[0] == '-':
            a,b = divmod(length_S, K)
            if b == 0:
                return a
            else:
                return "IMPOSSIBLE"
    return reverse_part(S, K)

if __name__ == "__main__":
    
    """The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom."""
    T = int(raw_input())
    for i in xrange(1, T+1):
        n, m = [s for s in raw_input().split(" ")] #$f.readline().strip()
        solution = solve(n,m)
        print("Case #{0}: {1}".format(i, solution))