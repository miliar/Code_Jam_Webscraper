from __future__ import print_function
import collections
import heapq
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

T = int(f.readline().strip())

def calc(N, M):
    min_req_speed = 0

    total1 = 0
    for i in xrange(N-1):
        delta = M[i+1] - M[i]
        x = abs(min(delta, 0))
        total1 += x
        min_req_speed = max(min_req_speed, x)

    total2 = 0
    for i in xrange(N-1):
        x = min(min_req_speed, M[i])
        # print(i, x)
        total2 += x

    return total1, total2

for case_id in range(1, T+1):
    N = int(f.readline().strip())
    M = map(int, f.readline().strip().split())

    r = calc(N, M)
    print(str.format('Case #{0}: {1} {2}', case_id, r[0], r[1]))
