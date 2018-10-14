#!/usr/bin/python

import sys
import operator

def solve(candies, taken, left_xor, left_sum, right_xor, right_sum, took):
    max_ = -1

    if left_xor == right_xor and left_sum != 0 and right_sum != 0:
        return 1
        max_ = max(left_sum, right_sum)
        return max_


    for i in range(0, N):
        if not taken[i]:
            taken[i] = True
            left_xor  ^= candies[i]
            right_xor ^= candies[i]
            left_sum  += candies[i]
            right_sum -= candies[i]

            if solve(candies, taken, left_xor, left_sum, right_xor, right_sum, i) != -1:
                return 1

            left_xor  ^= candies[i]
            right_xor ^= candies[i]
            left_sum  -= candies[i]
            right_sum += candies[i]
            taken[i] = False

    return -1

def patrick(l):
    return reduce(operator.__xor__, l, 0)

def partition(candies, taken):
    left = []
    right = []
    for c,t in zip(candies,taken):
        if t:
            left.append(c)
        else:
            right.append(c)
    return (left, right)
    

def solve2(canides, taken, N, took):
    for i in range(took+1, N):
        if not taken[i]:
            taken[i] = True
            left, right = partition(candies, taken)
            if left and right and patrick(left) == patrick(right):
                return 1
            if solve2(candies, taken, N, i) == 1:
                return 1
            taken[i] = False
    return -1


T = int(sys.stdin.readline())
for test_case in range(T):
    N = int(sys.stdin.readline())
    candies = [ int(c_str) for c_str in sys.stdin.readline().strip().split() ]
    taken = [ False ] * N

    left_xor = left_sum = 0
    right_xor = reduce(operator.__xor__, candies, 0)
    right_sum = sum(candies)

    #answer = solve(candies, taken, left_xor, left_sum, right_xor, right_sum, -1)
    answer = solve2(candies, taken, N, -1)

    print 'Case #%d:' % (test_case+1),
    if answer == -1:
        print 'NO'
    else:
        print sum(candies) - min(candies)
