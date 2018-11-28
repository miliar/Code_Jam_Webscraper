#-*- encoding: utf-8 -*-
import sys

def xor(a, b):
    return a^b

def solve(candies):
    splittable = reduce(xor, candies) == 0
    if not splittable:
        return "NO"

    return sum(candies[1:])

if '__main__' == __name__:
    T = int(sys.stdin.readline().strip())

    for case_n in xrange(T):
        N = int(sys.stdin.readline().strip())
        candies = sorted(int(x) for x in sys.stdin.readline().strip().split())
        solution = solve(candies)

        print('Case #%d: %s' % (case_n+1, solution))
