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
# from queue import PriorityQueue  # q = PriorityQueue(); q.put((pr1, pr2, ...)); item = q.get()
# from itertools import combinations
# from itertools import permutations
# from functools import lru_cache  # @lru_cache(maxsize=None)
from copy import copy, deepcopy
# from sys import stdin, stdout
from sys import maxsize  # 9 * 10**18
# inf = float('inf')

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        AC, AJ = map(int, input().strip().split(' '))

        CD = []
        for i in range(AC):
            CD.append(list(map(int, input().strip().split(' '))))

        JK = []
        for i in range(AJ):
            JK.append(list(map(int, input().strip().split(' '))))

        ans = solve(AC, AJ, CD, JK)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(AC, AJ, CD, JK):
    total_mins = 1440
    half_mins = 720

    # print(AC, AJ, CD, JK)

    acts =  []
    c_span = 0
    j_span = 0
    for a in CD:
        acts.append((a, 1))
        c_span += a[1] - a[0]
    for a in JK:
        acts.append((a, 2))
        j_span += a[1] - a[0]

    acts.sort(key=lambda t: t[0][0])

    # print(acts)
    # print(c_span, j_span)

    can_merge = [False] * len(acts)


    # def get_act_span(act):
    #     return act[0][1] - act[0][0]

    def get_exchange(acts):
        if len(acts) == 1:
            return 2

        exc = 0
        l = len(acts)
        for i in range(l):
            if acts[(i+1)%l][1] != acts[i][1]:
                exc += 1
            else:
                exc += 2
        return exc

    # try all possible merge
    def merge(acts, idx, spans):
        if spans[1] > 720 or spans[2] > 720:
            return maxsize

        # if idx == len(acts):
        #     return get_exchange(acts)

        min_exc = maxsize
        l = len(acts)
        while idx < l:
            next_idx = (idx+1) % l
            if acts[idx][1] != acts[next_idx][1]:
                idx += 1
                continue
            else:
                # try merge idx and next_idx
                new_acts = deepcopy(acts)
                new_spans = copy(spans)

                if next_idx == idx+1:
                    span = acts[next_idx][0][0] - acts[idx][0][1]
                else:
                    span = acts[next_idx][0][0] + 1440 - acts[idx][0][1]
                new_spans[acts[next_idx][1]] += span
                # # if use shallow copy
                # act = (list(acts[idx][0]), acts[idx][1])
                # new_acts.pop(idx)
                # new_acts.insert(idx, act)
                # new_acts.pop(next_idx)

                new_acts[idx][0][1] = acts[next_idx][0][0]
                new_acts.pop(next_idx)
                exc = merge(new_acts, idx, new_spans)
                min_exc = min(min_exc, exc)

                # and try not merge
                idx += 1
                continue

        min_exc = min(min_exc, get_exchange(acts))
        return min_exc

    return merge(acts, 0, [0, c_span, j_span])


if __name__ == '__main__':
    main()
