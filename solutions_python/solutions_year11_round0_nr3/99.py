#!/usr/bin/python3

from sys import argv
from functools import reduce

infile = open(argv[1])
cases = int(infile.readline())

for i in range(0, cases):
    n = int(infile.readline())
    vals = list(map(int, infile.readline().split()))
    p = reduce(lambda a,b: a^b, vals, 0)
    m = sum(vals) - min(vals)
    print('Case #{}: {}'.format(i+1,m if p==0 else 'NO'))
