#!/usr/bin/env python
import sys
import math


def problem(fi):
    n, k = fi.readline().strip().split(' ')
    pancakes = []
    for i in xrange(int(n)):
        r, h = fi.readline().strip().split(' ')
        pancakes.append((int(r), int(h)))
    return int(n), int(k), pancakes


def area(stack):
    area = 0.0
    for i in xrange(len(stack) - 1, 0, -1):
        r2, h2 = stack[i]
        r1, h1 = stack[i - 1]
        area += math.pi * ((r1 * r1) - (r2 * r2) + (2 * r2 * h2))

    r, h = stack[0]
    area += math.pi * 2 * r * h

    r, h = stack[-1]
    area += math.pi * r * r

    return area


def solve(params, i):
    n, k, pancakes = params

    pancakes.sort(reverse=True)

    stack = []
    for i in xrange(n):
        if len(stack) < k:
            stack.append(pancakes[i])
        else:

            max_stack_area = area(stack)
            next_stack = stack

            for j in xrange(k):

                new_stack = stack[0:j] + stack[j + 1:] + [pancakes[i]]
                stack_area = area(new_stack)
                if stack_area > max_stack_area:
                    max_stack_area = stack_area
                    next_stack = new_stack

            stack = next_stack

    return '{:.9f}'.format(area(stack))


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
