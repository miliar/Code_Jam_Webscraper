import sys
import math

from decimal import *

def best(pancakes, stack):
    a_r = []
    for i in range(pancakes):
        radius, height = file.readline().split(' ')
        a_r += [(float(height)*float(radius), float(radius), i)]

    a_r = sorted(a_r)
    best = 0
    for a0, r0, i0 in a_r:
        a_sum = a0
        count = 1
        for a1, r1, i1 in reversed(a_r):
            if count == stack:
                break
            if i1 == i0:
                continue
            if r1 <= r0:
                a_sum += a1
                count += 1
        result = (math.pi * ((r0*r0) + (a_sum*2)))
        #print('{} {} {}'.format(r0, a_sum, result))
        if result > best:
            best = result
    return best

file_name = sys.argv[1]
with open(file_name) as file:
    T = int(file.readline())
    for x in range(T):
        pancakes, stack = file.readline().split(' ')
        print('Case #{}: {}'.format(x+1, format(best(int(pancakes), int(stack)), '.10f')))
