from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'A-large.in'

def other(sgn):
    return '+' if sgn == '-' else '-'

def _solve(s, k):
    i = 0
    s = list(s)
    res = 0
    while True:
        if i + k > len(s):
            break
        if s[i] == '-':
            res += 1
            for j in range(i, i+k):
                s[j] = other(s[j])
        i += 1
    for i in range(len(s) - k, len(s)):
        if s[i] == '-':
            return 'IMPOSSIBLE'
    return res

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
    (s, k) = tuple(inp_file.readline().split())
    k = int(k)
    res = solve(s, k)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()









