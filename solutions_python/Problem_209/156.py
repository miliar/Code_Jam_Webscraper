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
from math import pi
# import time  # start_time = time.time(); elapsed_time = time.time() - start_time
# from collections import Counter
# from collections import OrderedDict
# from collections import deque
# from queue import PriorityQueue  # q = PriorityQueue(); q.put((pr1, pr2, ...)); item = q.get()
# from itertools import combinations
# from itertools import permutations
from functools import lru_cache  # @lru_cache(maxsize=None)
# from copy import copy, deepcopy
# from sys import stdin, stdout
# from sys import maxsize  # 9 * 10**18
# inf = float('inf')

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        # read multiple integers (known length)
        N, K = map(int, input().strip().split(' '))

        RH = []
        for i in range(N):
            RH.append(list(map(int, input().strip().split(' '))))

        ans = solve(N, K, RH)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(N, K, RH):
    # print(N, K, RH)

    RH.sort(reverse=True, key=lambda i: i[0])
    # print(RH)

    def get_side_area(rh):
        r, h = rh
        return 2 * pi * r * h

    side_areas = list(map(get_side_area, RH))

    max_area = 0
    for i in range(N):
        # assume take i as bottom piece
        if i > N - K:
            break

        r, h = RH[i]
        area = 0
        area += pi * r * r
        area += side_areas[i]

        sorted_sa = sorted(side_areas[i+1:], reverse=True)
        area += sum(sorted_sa[:K-1])

        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    main()
