#!/usr/bin/env python

import sys

def solve(D, N, KS):
    T = []
    for h in KS:
        T.append((D - h[0]) / h[1])
    
    return D/max(T)


def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):
        
        print("Processing Case #{}".format(case_counter), file =sys.stderr)
        
        # INPUT
        D, N = [int(s) for s in input().split(" ")]

        KS = []
        for i in range(N):
            KS.append([int(s) for s in input().split(" ")])

        print("KS", KS, file =sys.stderr)

        # SOLVE
        solution = solve(D, N, KS)

        # OUTPUT
        print("Case #{}: {}".format(case_counter, solution))

        case_counter += 1


if  __name__ =='__main__':
    main()
