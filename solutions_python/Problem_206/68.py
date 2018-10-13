from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'A-large.in'

def _solve(d, horses):
    mx = 10**100
    for s, k in horses:
        mx = min(mx, d / ((d - s) / k))
    return mx

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    (d,n) = tuple(map(int, inp_file.readline().split()))
    horses = []
    for _ in range(n):
        horses.append(tuple(map(int, inp_file.readline().split())))
    res = solve(d, horses)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()









