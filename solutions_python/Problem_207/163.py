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
# import math
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
        N, R, O, Y, G, B, V = map(int, input().strip().split(' '))

        ans = solve(N, R, O, Y, G, B, V)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(N, R, O, Y, G, B, V):
    allColors = {
        'R': R,
        'O': O,
        'Y': Y,
        'G': G,
        'B': B,
        'V': V
    }

    if R < G or Y < V or B < O:
        return 'IMPOSSIBLE'

    # consider RGRGRG
    if R == G > 0:
        if O == Y == B == V == 0:
            return 'RG' * R
        else:
            return 'IMPOSSIBLE'

    if Y == V > 0:
        if R == O == G == B == 0:
            return 'YV' * Y
        else:
            return 'IMPOSSIBLE'

    if B == O > 0:
        if R == Y == G == V == 0:
            return 'BO' * B
        else:
            return 'IMPOSSIBLE'


    colors = [[R - G, 'R'], [Y - V, 'Y'], [B - O, 'B']]
    colors.sort(reverse=True)
    # print(colors)

    oppositeColor = {'R': 'G', 'Y': 'V', 'B': 'O'}

    for i in range(3):
        if colors[i][0] < 0:
            return 'IMPOSSIBLE'

    if colors[0][0] > (colors[1][0] + colors[2][0]):
        return 'IMPOSSIBLE'
    else:
        # possible
        ans = ''

        d = (colors[1][0] + colors[2][0]) - colors[0][0]

        # use all the composite colors
        if d > 0:
            for i in range(3):
                c = colors[i][1]
                oc = oppositeColor[c]
                ans += c + (oc + c) * allColors[oc]
                colors[i][0] -= 1
        else:  # d == 0
            for i in [0, 1]:
                c = colors[i][1]
                oc = oppositeColor[c]
                ans += c + (oc + c) * allColors[oc]
                colors[i][0] -= 1
            if colors[2][0] > 0:
                ans += colors[0][1]
                colors[0][0] -= 1

                for i in [2]:
                    c = colors[i][1]
                    oc = oppositeColor[c]
                    ans += c + (oc + c) * allColors[oc]
                    colors[i][0] -= 1
        # use basic colors
        d = (colors[1][0] + colors[2][0]) - colors[0][0]

        ans += (colors[0][1] + colors[1][1] + colors[2][1]) * d
        for i in range(3):
            colors[i][0] -= d

        ans += (colors[0][1] + colors[1][1]) * colors[1][0]
        # colors[0][0] -= colors[1][0]
        # colors[1][0] -= colors[1][0]

        ans += (colors[0][1] + colors[2][1]) * colors[2][0]

        return ans


if __name__ == '__main__':
    main()
