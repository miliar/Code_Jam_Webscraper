#!/bin/python

import sys


# def flip(S, ind, K):
#     if ind<0 or ind+K > len(S): return None
#     for i in range(ind, ind+K+1):
#         S[i] = not S[i]

def solve(S, K, count):
    if len(S) == 0: return str(count)
    if len(S) < K: return 'IMPOSSIBLE'
    # print S, K, count

    left = 0
    right = len(S)-1
    if not S[left]:
        for i in range(left, left + K):
            S[i] = not S[i]
        count += 1

    if not S[right]:
        for i in range(right-K+1, right+1):
            S[i] = not S[i]
        count += 1

    # print S, K, count
    while left < len(S) and S[left]: left += 1
    while right >= 0 and S[right]: right -= 1
    # print left, right
    return solve(S[left:right + 1], K, count)


T = int(raw_input().strip())

for c in range(1, T + 1):
    S, K = raw_input().split()
    S = map(lambda x: False if x == '-' else True, S)
    K = int(K)
    ans = solve(S, K, 0)
    print 'Case #' + str(c) + ': ' + ans
