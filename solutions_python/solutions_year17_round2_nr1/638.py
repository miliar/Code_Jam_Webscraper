#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

def run():
    D, N = map(int,input.readline().split())
    M = 0
    for i in range(N):
        Ki, Si = map(int,input.readline().split())
        x = (float(D)-Ki)/Si
        if x > M:
            M = x
    return D/M

T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run())
