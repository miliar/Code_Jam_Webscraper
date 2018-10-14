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
    d, n = map(int, input().split())
    slo = -1
    for i in range(n):
        ki, si = map(int, input().split())
        slo = max((d-ki)/si, slo)

    print('Case #%d:' % case, end=' ')
    print('%.6f' % (d/slo))
