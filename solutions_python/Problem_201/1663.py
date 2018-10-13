#!/usr/bin/env python

import sys
import math

def process_input():
    with open("C-large.in") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def compute_single_case(N, K, global_counter):
    exp = 0
    if K == 1:
        exp = 0
    elif K == 2:
        exp = 1
    else:
        dup_K = K
        while dup_K > 0:
            dup_K /= 2
            exp += 1
        exp -= 1
    left_over = 0
    if K == 0:
        left_over = 0
    elif K == 1:
        left_over = 0
    else:
        math_val = 1
        dup_exp = exp
        while dup_exp > 0:
            math_val *= 2
            dup_exp -= 1
        left_over = K - math_val
    # print "K=" + str(K), "exp=", exp, "left_over", left_over, K == (2**exp) + left_over
    exp_total = 2**exp
    N = N - (exp_total - 1)
    lower = N / exp_total
    higher_counter = N % exp_total

    if (left_over) < higher_counter:
        r = lower + 1
    else:
        r = lower
    if r % 2 == 1:
        print "Case #" + str(global_counter) + ":", r / 2, r / 2
    else:
        print "Case #" + str(global_counter) + ":", r / 2, r / 2 - 1

from heapq import heappush, heappop

def main():
    content = process_input()
    data_size = int(content.pop(0))
    global_counter = 0

    for line in content:
        [N, K] = [int(x) for x in line.split(' ')]
        # print N, K
        global_counter += 1
        compute_single_case(N,K, global_counter)

main()
