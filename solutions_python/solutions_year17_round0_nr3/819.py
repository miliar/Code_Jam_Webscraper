from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
from collections import defaultdict
from heapq import heappush, heappop
#inf = 10**20

name = 'C-large.in'
#name = 'micro.in'

def _solve(stalls, people):
    queues = [-stalls]
    qs = defaultdict(lambda : 0)
    qs[stalls] += 1
    while True:
        length = -heappop(queues)
        quantity = qs[length]
        l1 = (length - 1) // 2
        l2 = length // 2
        if quantity < people:
            qs[length] == 0
            for l in [l1, l2]:
                if l != 0:
                    if qs[l] == 0:
                        heappush(queues, -l)
                    qs[l] += quantity
            people -= quantity
        else:
            return ' '.join(map(str, reversed(sorted((l1, l2)))))


def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

#print(solve(10**18,10**18 // 10))
#import sys
#sys.exit()

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    (s, p) = tuple(map(int, inp_file.readline().split()))
    res = solve(s, p)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()
