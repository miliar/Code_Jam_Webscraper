from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import math
import sys


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        n, p = map(int, sys.stdin.readline().split())
        g = tuple(map(int, sys.stdin.readline().split()))
        cnt = 0
        if p == 2:
            for i in g:
                if i % 2 == 0:
                    cnt += 1
            for i in g:
                if i % 2 != 0:
                    cnt += 0.5
            cnt = math.ceil(cnt)
        elif p == 3:
            left1 = 0
            left2 = 0
            for i in g:
                if i % 3 == 0:
                    cnt += 1
                elif i % 3 == 1:
                    left1 += 1
                else:
                    left2 += 1
            cnt += min(left1, left2)
            cnt += math.ceil((max(left1, left2) - min(left1, left2)) / 3)
        else:
            left1 = 0
            left2 = 0
            left3 = 0
            for i in g:
                if i % 4 == 0:
                    cnt += 1
                elif i % 4 == 1:
                    left1 += 1
                elif i % 4 == 2:
                    left2 += 1
                else:
                    left3 += 1
            cnt += left2 // 2
            cnt += min(left1, left3)
            left13 = max(left1, left3) - min(left1, left3)
            if left2 % 2 == 1:
                if 2 <= left13:
                    left13 -= 2
                    cnt += 1
                else:
                    left13 = 0
                    cnt += 1
            cnt += math.ceil(left13 / 4)
        print('Case #{}: {}'.format(case + 1, int(cnt)))


if __name__ == '__main__':
    main()
