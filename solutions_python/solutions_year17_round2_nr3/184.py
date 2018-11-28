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
    n, q = map(int, input().split())
    e, s = [], []
    for _ in range(n):
        ei, si = map(int, input().split())
        e.append(ei)
        s.append(si)

    g = defaultdict(list)
    w = defaultdict(dict)
    for i in range(n):
        row = map(int, input().split())
        for j, v in enumerate(row):
            if v == -1:
                continue
            g[i].append(j)
            w[i][j] = v
    
    uv = []
    for _ in range(q):
        uk, vk = map(int, input().split())
        uv.append( (uk-1, vk-1) )

    rem = [None for _ in range(n)]
    rem[-1] = 0
    for i in range(n-2, -1, -1):
        prev = rem[i+1]
        edge = w[i][i+1]
        rem[i] = edge + prev

    reachable = defaultdict(list)
    dist = defaultdict(dict)
    for i in range(n):
        dd = 0
        for j in range(i+1, n):
            dd += w[j-1][j]
            if dd > e[i]:
                break
            reachable[i].append(j)
            dist[i][j] = dd
    for i in range(n):
        dd = 0
        for j in range(i+1, n):
            dd += w[j-1][j]
            dist[i][j] = dd
    for i in range(n):
        dist[i][i] = 0
    #print(dist)

    dp = [None for _ in range(n)]
    dp[-1] = 0
    for i in range(n-2, -1, -1):
        minn = float('inf')
        for r in reachable[i]:
            #print(i, rem[i], dist[r][n-1])
            minn = min(dp[r] + (rem[i]-dist[r][n-1])/s[i], minn)
        dp[i] = minn
    
    print('Case #%d:' % case, end=' ')
    print(dp[0])
