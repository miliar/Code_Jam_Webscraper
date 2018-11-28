from itertools import product
from operator import xor

def sean_sum(xs):
    return reduce(xor, xs, 0)

def value(xs, cc):
    left = [x for x, c in zip(xs, cc) if c]
    right = [x for x, c in zip(xs, cc) if not c]
    if left and right and sean_sum(left) == sean_sum(right):
        return max(sum(left), sum(right))
    else:
        return -1

def solve_brutal(xs):
    nx = len(xs)
    m = max(value(xs, cc) for cc in product((0,1), repeat=nx))
    return str(m) if m != -1 else 'NO'

def solve(xs):
    if xs and sean_sum(xs) == 0:
        return sum(xs) - min(xs)
    else:
        return 'NO'

def main(L):
    for t in range(1, 1 + int(L[0])):
        print 'Case #%d: %s' % (t, solve(map(int, L[2*t].split())))

import sys
main(list(sys.stdin))
