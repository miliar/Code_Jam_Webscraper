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
        R, C = map(int, input().strip().split(' '))

        Cake = []
        for rowIdx in range(R):
            Cake.append(input().strip())

        ans = solve(R, C, Cake)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(R, C, Cake):
    # print(Cake)
    ans = []

    firstNotAllQRow = 0

    for ri in range(R):
        rowAns = ""
        isAllQuestion = True
        for ci in range(C):
            c = Cake[ri][ci]
            if c != '?':
                if isAllQuestion:
                    isAllQuestion = False
                    rowAns = c * (ci + 1)
                else:
                    rowAns = rowAns + c
                prevChar = c
            else:  # is '?'
                if isAllQuestion:  # so far all ?
                    continue
                else:
                    rowAns = rowAns + prevChar

        if isAllQuestion:
            # copy last row
            if ri == 0:
                ans.append(Cake[0])
            else:
                ans.append(ans[ri-1])
        else:
            ans.append(rowAns)

    for ri in range(R-2, -1, -1):
        if ans[ri][0] == '?':
            ans[ri] = ans[ri+1]

    # print(ans)

    a = '\n' + '\n'.join(ans)

    return a


if __name__ == '__main__':
    main()
