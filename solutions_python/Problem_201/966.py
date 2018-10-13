#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

def solve(N, K):
    d = defaultdict(int)
    d[N]=1
    while True:
        print d, K
        n = max(d.keys())
        nn = (n-1)//2
        mm = n - 1 - nn
        assert mm + nn + 1 == n
        count = d[n]
        del d[n]
        d[nn] += count
        d[mm] += count
        K -= count
        if K <= 0:
            return "{} {}".format(mm, nn)
        
def run():
    N, K = map(int, input.readline().split(' '))
    return solve(N, K)

T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run())
