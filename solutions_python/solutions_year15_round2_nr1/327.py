#!/bin/env python3

tree = {}
global clist
clist = [1]

def rev(n):
    sr = str(n)[::-1]
    r = int(sr)
    return r 

def rec(C,goal):
    global tree

    while goal not in tree:
        #print(C)
        nC = []
        for c in C:
            if c+1 in tree:
                pass
            else:
                #print(tree)
                tree[c+1] = tree[c] + 1
                nC += [c+1]
            
            r = rev(c)
            if r in tree:
                pass
            else:
                tree[r] = tree[c] + 1
                nC += [r]
        C = nC

    return tree[goal],C

def solution(N):
    global tree
    global clist
    #tree = {}
    tree[1] = 1

    count,theclist = rec(clist,N)
    clist = theclist

    return (count,)


#%% Main and input handling

def main():
    T = int(input())
    
    for t in range(T):
        do_case(t+1)

import time

def do_case(t):
    N = int(input())
    #P = [int(x) for x in input().split()]
    
    answers = solution(N)
    print_case(t, answers)
    
def print_case(t,answers):
    print("Case #%d: %d" % ((t,)+answers))

if __name__ == "__main__":
    main()
