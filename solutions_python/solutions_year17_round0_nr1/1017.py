# import numpy as np
# import networkx as nx
# import re
# import math
# from collections import Counter
# from collections import OrderedDict
# from itertools import combinations
# from itertools import permutations

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        S, K = input().strip().split(' ')
        K = int(K)

        ans = solve(S, K)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(S, K):
    SBool = [False if side == '-' else True for side in S]
    # print(SBool)
    # print(K)
    flipCount = 0

    for i in range(len(SBool) - K + 1):  # range(0, 5-3) = [0, 1, 2]
        if SBool[i] == False:
            for j in range(K):
                SBool[i+j] = not SBool[i+j]
            flipCount += 1
    for i in range(len(SBool) - K + 1, len(SBool)):
        if SBool[i] == False:
            return 'IMPOSSIBLE'

    return flipCount

if __name__ == '__main__':
    main()
