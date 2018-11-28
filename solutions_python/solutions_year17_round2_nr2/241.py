import sys

from itertools import *
from math import *
from collections import deque, defaultdict, OrderedDict
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

for case in range(1, int(input())+1):
    n, r, o, y, g, b, v = map(int, input().split())

    if r/n > 0.5 or b/n > 0.5 or y/n > 0.5:
        ans = 'IMPOSSIBLE'
    else:
        ans = []
        last = None
        c = {'R': r, 'B': b, 'Y': y}
        i = 0
        while i < n:
            od = sorted(c.items(), key=itemgetter(1), reverse=True)
            hi = od[0][0] if od[0][0] != last else od[1][0]
            ans.append(hi)
            c[hi] -= 1
            i += 1
            last = hi
        if ans[0] == ans[-1]:
            ans[-1], ans[-2] = ans[-2], ans[-1]
        ans = ''.join(ans)

    print('Case #%d:' % case, end=' ')
    print(ans)
