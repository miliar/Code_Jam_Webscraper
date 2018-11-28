from __future__ import print_function
import collections
import heapq
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

T = int(f.readline().strip())

def calc(item):
    if -item[0] == 1: # End case.
        return 1

    # Simple.
    r0 = calc([x+1 for x in item if x < -1])

    # Specials.
    max_num = -heapq.heappop(item)
    assert max_num > 1
    k = max_num // 2
    for a in range(2, k+1):
        b = max_num - a
        new_item = list(item)
        heapq.heappush(new_item, -a)
        heapq.heappush(new_item, -b)
        r0 = min(r0, calc(new_item))

    return r0 + 1

for case_id in range(1, T+1):
    num_diners = int(f.readline().strip())
    cakes = [int(x) for x in f.readline().strip().split()]
    #~ print(cakes)

    start_item = [-x for x in cakes]
    heapq.heapify(start_item)
    r = calc(start_item)

    print(str.format('Case #{0}: {1}', case_id, r))
