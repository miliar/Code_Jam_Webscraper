#!/usr/bin/env python

def flipPancakes(S,K,i):
    for n in range(K):
        S[i+n] = '-' if S[i+n] == '+' else '+'


def isValid(S):
    for p in S:
        if p == '-':
            return False
    
    return True


def solve(S, K):
    flipNum = 0
    for i, p in enumerate(S) :
        if p == '-' and i+K <= len(S) :
            flipPancakes(S,K,i)
            flipNum += 1
        # print(S)
    
    if isValid(S):
        return str(flipNum)
    
    return "IMPOSSIBLE"


def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):
        
        M = []
        
        # Read the data
        (S, K) = input().split(" ")
        S = list(S)
        K = int(K) 
        # print(S)
        # print(K)

        print("Case #{}: {}".format(case_counter, solve(S, K)))
        case_counter += 1


if  __name__ =='__main__':
    main()
