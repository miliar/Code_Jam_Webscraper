#!/usr/bin/env python3


def flip(stove, index, spatula):
    for i in range(index, index + spatula):
        stove[i] = not stove[i]


def brute_force(stove, spatula):
    n = len(stove) - spatula + 1
    mini = float('inf')
    for i in range(2**n):
        try_flip = stove[:]
        count = 0
        for j in range(n):
            if (1 << j) & i:
                count += 1
                flip(try_flip, j, spatula)
        if all(try_flip):
            mini = min(mini, count)
    return str(mini) if mini != float('inf') else 'IMPOSSIBLE'


def try_optimum(stove, spatula):
    n = len(stove) - spatula + 1
    count = 0
    for i in range(n):
        if not stove[i]:
            count += 1
            flip(stove, i, spatula)
    if all(stove):
        return str(count)
    else:
        return 'IMPOSSIBLE'


def compare_brute_and_optimum():
    upto = 10
    for len_S in range(2, upto + 1):
        for i in range(2**len_S):
            stove = []
            for j in range(len_S):
                stove.append(bool((1 << j) & i))
            for K in range(2, len_S + 1):
                brute = brute_force(stove[:], K)
                optimum = try_optimum(stove[:], K)
                if brute != optimum:
                    print('brute', brute, 'optimum', optimum, 'K', K)
                    pstove(stove)

def pstove(stove):
    print(''.join('1' if x else '0' for x in stove))

T = int(input())
for i in range(T):
    st, spatula = input().split()
    stove = []
    for s in st:
        if s == '+':
            stove.append(True)
        else:
            stove.append(False)
    spatula = int(spatula)
    answer = try_optimum(stove, spatula)
    print("Case #" + str(i + 1) + ': ' + answer)
