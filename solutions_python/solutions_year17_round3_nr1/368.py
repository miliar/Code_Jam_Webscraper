import math
from collections import namedtuple
Pancake = namedtuple('Pancake', ['r', 'h'])

def area_cake(cake):
    return math.pi * (cake.r ** 2)

def high_area_cake(cake):
    return 2 * math.pi * (cake.r * cake.h)

def replace_cake(last, bigest, cur):
    change = area_cake(cur) + high_area_cake(cur) - area_cake(bigest) - high_area_cake(last_cake)
    if change <= 0:
        return last, bigest
    else:
        return cur, cur

def calc(cakes):
    sum = 0
    for c in cakes:
        sum+=high_area_cake(c)
    bigest_cake = max(cakes, key = lambda x: x.r)
    sum+=area_cake(bigest_cake)
    return sum

T = int(input())
for i in range(T):
    cakes = []
    N, K = input().split()
    N = int(N)
    K = int(K)
    for j in range(N):
        r, h = input().split()
        cakes.append(Pancake(int(r), int(h)))
    sorted_cakes = sorted(cakes, key = lambda x: -x.r * x.h)
    last_cake = sorted_cakes[K-1]
    bigest_cake = max(sorted_cakes[:K], key = lambda x: x.r)
    for rest in range(K,N):
        last_cake, bigest_cake=replace_cake(last_cake, bigest_cake, sorted_cakes[rest])
    print('Case #{0}: {1}'.format(i+1, calc(sorted_cakes[:K-1] + [last_cake])))
