import sys
import math
import itertools
import heapq
from collections import deque


def area_of_side(r, h):
    return 2 * math.pi * r * h

def area_of_top(r):
    return math.pi * r * r

def area(p1, p2=(0, 0)):
    p1_side = area_of_side(*p1)
    p1_top = area_of_top(p1[0])
    p2_top = area_of_top(p2[0])
    return p1_side + p1_top - p2_top

def min_pancake_area(pancakes):
    p_pairs = itertools.zip_longest(pancakes, pancakes[1:], fillvalue=(0,0))
    for p1, p2 in p_pairs:
        yield area(p1, p2)


def solve(n, k, pancakes):
    heap = deque((1.0/area(p), {i}) for i, p in enumerate(pancakes))
    #heapq.heapify(heap)
    maxa = 0
    while heap:
        #a, pset = heapq.heappop(heap)
        a, pset = heap.popleft()
        a = 1.0/a
        if len(pset) == k+1:
            break
        #print(pset, a, maxa)
        maxa = max(maxa, a)
        top = max(pset)
        for i, p in enumerate(pancakes[top:], start=top):
            if i not in pset:
                new_set = pset.copy()
                new_set.add(i)
                new_area = a + area(p) - area_of_top(p[0])
                heap.append((1.0/new_area, new_set))
                #heapq.heappush(heap, (1.0/new_area, new_set))
    return maxa



if __name__=="__main__":
    lines = iter(open(sys.argv[1]))
    next(lines)
    for i, l in enumerate(lines, start=1):
        n, k = map(int, l.split())
        pancakes = [tuple(map(int, next(lines).split())) for _ in range(n)]
        pancakes.sort(reverse=True)
        print("Case #{}: {}".format(i, solve(n, k, pancakes)))
