
# -*- coding: utf-8 -*-

import itertools


def refresh_lr(L, R, S, _from, _to):
    for i in range(_from, _to):
        (L[i], R[i]) = look_LR(S, i)


def look_LR(S, j):
    L = R = 0
    for i in range(j - 1, -1, -1):
        if S[i]:
            break
        else:
            L += 1

    for i in range(j + 1, len(S)+1, 1):
        if S[i]:
            break
        else:
            R += 1
    return (min(L, R), max(L, R))


T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split(" ")]
    N2 = N + 2
    S = [False] * N2
    S[0] = S[N2-1] = True
    #L = [0] * N2
    #R = [0] * N2
    # refresh_lr(L, R, S, 1, N2-1)
    # print(S)
    
    for i in range(K):
        currentMin = -1
        currentMax = -1
        currentCand = -1
        for j in range(N2):
            if S[j]:
                # occupied!
                continue
            else:
                # _min, _max = (min(L[j], R[j]), max(L[j], R[j]))
                _min, _max = look_LR(S, j)
                if(_min > currentMin):
                    currentMin = _min
                    currentMax = _max
                    currentCand = j
                elif(_min == currentMin and _max > currentMax):
                    currentMin = _min
                    currentMax = _max
                    currentCand = j
        S[currentCand] = True
        # refresh_lr(L, R, S, currentCand - L[j], currentCand + R[j])
        # print(S)

    print("Case #" + str(t + 1) + ": " + str(currentMax) + " " + str(currentMin))
