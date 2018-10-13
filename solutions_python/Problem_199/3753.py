
# -*- coding: utf-8 -*-

import itertools
import sys


def is_odd(num):
    return num & 0x1


def is_smile(pancakes, flip_pos, k):
    my_pancakes = pancakes[:]
    for i, b in enumerate(flip_pos):
        if b:
            for j in range(K):
                my_pancakes[i + j] = not my_pancakes[i + j]
    return all(my_pancakes)


def count_flips(flip_pos):
    return sum([1 for x in flip_pos if x])


def count_non_smiles(pancakes):
    return len(pancakes) - count_flips(pancakes)


T = int(input())
for t in range(T):
    result = sys.maxsize
    s = input()
    (S, K) = s.split(" ")
    N = len(S)
    K = int(K)
    pancakes = []
    for p in S:
        pancakes.append(p == "+")
    n_cand_pos = N - (K - 1)

    if(all(pancakes)):
        result = 0
    # elif(is_odd(K) != is_odd(count_non_smiles(pancakes))):
    #    pass    # There is no answer
    else:
        for cand in itertools.product([False, True], repeat=n_cand_pos):
            if(is_smile(pancakes, cand, K)):
                result = min(result, count_flips(cand))

    result = str(result) if result < sys.maxsize else "IMPOSSIBLE"
    print("Case #" + str(t + 1) + ": " + result)
