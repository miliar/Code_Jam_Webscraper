import math
from decimal import *
def find_area(r, h):
    a = r * r + 2 * r * h
    return a

def find_stack(cakes, k):
    cakes.sort(key=lambda x: (x[2],x[0]))
    prev_a = 0
    total_a = 0
    res = []
    for i in xrange(len(cakes) - k, len(cakes)):
        res.append(cakes[i])

    res.sort(key=lambda x: x[0])
    for cake in res:
        total_a += cake[2] - prev_a
        prev_a = cake[0] * cake[0]
    #print total_a
    return Decimal((total_a) * Decimal(math.pi))


def find_area_cakes(selected_cakes):
    total_a = 0
    prev_a = 0
    for cake in selected_cakes:
        total_a += cake[2] - prev_a
        prev_a = cake[0] * cake[0]
    #print total_a
    return Decimal((total_a) * Decimal(math.pi))

def find_max(cakes, i, k, res, area, selected_cakes):
    if len(selected_cakes) == k:
        res[0] = max(find_area_cakes(selected_cakes), res[0])
        #print 'bf ', selected_cakes, res[0]
        return
    for j in xrange(i, len(cakes)):
        selected_cakes.append(cakes[j])
        find_max(cakes, j + 1, k, res, area, selected_cakes)
        selected_cakes.pop()


def find_stack_bf(cakes,k):
    cakes.sort(key=lambda x: x[0])
    res = [0]
    find_max(cakes, 0, k, res, 0, [])
    return res[0]





if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for case in xrange(1, t + 1):
        n, k = [int(x) for x in raw_input().split(' ')]
        cakes = []
        for i in xrange(n):
            r, h = [int(x) for x in raw_input().split(' ')]
            a = find_area(r, h)
            cakes.append((r, h, a))
        print 'Case #{}: {}'.format(case, find_stack_bf(cakes, k))