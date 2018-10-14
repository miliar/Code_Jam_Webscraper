import sys
import math

if __name__ == '__main__':

    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        c, f, x = map(float, sys.stdin.readline().strip().split())

        cost = 2.
        total_time = 0

        while c / cost + x / (cost + f) <= x / cost:
            total_time += (c / cost)
            cost += f

        print 'Case #{}: {}'.format(i + 1, total_time + (x / cost))
