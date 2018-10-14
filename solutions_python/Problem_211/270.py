#!/usr/bin/env python

import sys
from functools import reduce

def solve(N, K, U, P):
    average = (sum(P) + U) / N
    print(average, file =sys.stderr)

    new_sum = 0
    how_many = 0
    for p in P:
        if p <= average:
            new_sum += p
            how_many += 1
    print(new_sum, how_many, file =sys.stderr)

    if how_many == 0:
        new_average = 0
    else:    
        new_average = (new_sum + U) / how_many
    print(new_average, file =sys.stderr)

    for i, p in enumerate(P):
        if p <= average:
            P[i] = new_average
    
    print(P, file =sys.stderr)

    return reduce(lambda x, y: x*y, P)


def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):

        print("Processing Case #{}".format(case_counter), file =sys.stderr)
        
        # INPUT
        N, K = [int(s) for s in input().split(" ")]
        U = float(input())
        P = [float(s) for s in input().split(" ")]
        print(N, K, U, P, file =sys.stderr)

        # SOLVE
        solution = solve(N, K, U, P)

        # OUTPUT
        print("Case #{0}: {1:.9f}".format(case_counter, solution))

        case_counter += 1


if  __name__ =='__main__':
    main()
