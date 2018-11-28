import copy
import collections as c
import sys
from functools import reduce
import functools

def main():
    T = int(input())

    for T in range(T):
        A, B, K = [int(x) for x in input().split()]
        print("Case #{}: {}".format(T+1, solve(A, B, K)))
        
def solve(A, B, K):
    counter = 0
    for i in range(A):
        for j in range(B):
            if (i & j) < K:
                counter += 1
    return counter

if __name__ == '__main__':
    main()






