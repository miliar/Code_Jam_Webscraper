import sys
import numpy as np
from decimal import *

input_file = "C-small-1-attempt1.in"
output_file = "C-small-1-attempt1.out"

def prob_all_function(single_probs):
    chance = 1
    for single_prob in single_probs:
        chance *= single_prob
    return chance


def solve(tt):
    n, k = [int(j) for j in input().split(" ")]
    units = Decimal(input())
    p = [Decimal(j) for j in input().split(" ")]
    while units > 10**-8:
        p = sorted(p)
        d = np.diff(p)
        no_leading_zeros = 0
        if len(d) > 0:
            i = 0
            while d[i] == 0:
                no_leading_zeros += 1
                i += 1
                if i == n-1:
                    break
        else:
            i = 0
        if i >= n-1:
            d_after_zeros = 1-p[0]
        else:
            d_after_zeros = d[i]
        to_add = np.min([units, (no_leading_zeros+1)*d_after_zeros])/(no_leading_zeros+1)
        p[0] += to_add
        for i in range(1, no_leading_zeros+1):
            p[i] = p[i-1]
        units -= (no_leading_zeros+1)*to_add
    return(prob_all_function(p))

def main():
    t = int(input())
    for tt in range(1, t + 1):
        answer = solve(tt)
        print("Case #{}: {}".format(tt, answer))

if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()

#
# a = [0.50, 0.70, 0.80, 0.60, 0.40]
# print(prob_all_function(a))