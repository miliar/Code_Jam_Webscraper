"""
http://networkx.readthedocs.io/en/networkx-1.11/tutorial/index.html
https://docs.python.org/3/library/re.html
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/collections.html
https://docs.python.org/3/library/itertools.html
https://docs.python.org/3/library/functools.html#functools.lru_cache
"""

# import numpy as np
# import networkx as nx
# import re
import math
# import time  # start_time = time.time(); elapsed_time = time.time() - start_time
# from collections import Counter
# from collections import OrderedDict
# from collections import deque
# from itertools import combinations
# from itertools import permutations
# from functools import lru_cache
# from sys import stdin, stdout


def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        N, P = map(int, input().strip().split(' '))

        # recipe
        R = list(map(int, input().strip().split(' ')))

        Q = []
        for row in range(N):
            Q.append(list(map(int, input().strip().split(' '))))

        ans = solve(N, P, R, Q)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(N, P, R, Q):
    # print(N, P, R, Q)

    for q in Q:
        q.sort()

    # print(Q)

    servingRanges = [[countServing(Q[i][j], R[i]) for j in range(P)] for i in range(N)]

    # print(servingRanges)

    nIdx = 0
    notUsedPIdxs = [0] * N

    kitCount = 0

    def dfs(currRange, nIdx):
        if nIdx >= N:
            return True

        for pIdx in range(notUsedPIdxs[nIdx], P):

            rangeToMerge = servingRanges[nIdx][pIdx]

            if compareRange(rangeToMerge, currRange) == -1:
                # left
                continue
            elif compareRange(rangeToMerge, currRange) == 1:
                # right
                return False
            else:
                # overlap
                mergedRange = mergeRange(rangeToMerge, currRange)
                if not isValidRange(mergedRange):
                    continue

                isFormKit = dfs(mergedRange, nIdx + 1)

                if isFormKit:
                    notUsedPIdxs[nIdx] = pIdx + 1
                    return True
                else:
                    continue

    for pi in range(P):
        currRange = servingRanges[0][pi]
        if not isValidRange(currRange):
            continue

        isFormKit = dfs(currRange, 1)

        # print(notUsedPIdxs)

        if isFormKit:
            kitCount += 1

    return kitCount


def countServing(q, r):
    # r * max * 0.9 <= q <= r * min * 1.1
    mx = (q * 10) // (r * 9)  # int(math.floor((q * 10) / (r * 9)))
    mn = int(math.ceil((q * 10) / (r * 11)))
    # if mn > mx:
    #     return (0, 0)
    return (mn, mx)


def isValidRange(range):
    return range[1] >= range[0]

def mergeRange(range1, range2):
    return ( max(range1[0], range2[0]), min(range1[1], range2[1]) )

def compareRange(range1, range2):
    # r1 left to r2
    if range1[1] < range2[0]:
        return -1
    elif range1[0] > range2[1]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    main()
