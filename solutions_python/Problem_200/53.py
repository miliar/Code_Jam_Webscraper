#!/usr/bin/env python3

import os
import os.path
import sys
import time


if __name__ == '__main__':
    ans = '0' * 20
    t = int(input())
    for it in range(t):
        n = int(input())
        n = '{:020d}'.format(n)
        for pos in range(len(ans)):
            for dig in range(10):
                tmp = ans[:pos] + str(dig) * (len(ans) - pos)
                if tmp > n:
                    break
                ans = tmp

        print('Case #{}: {:d}'.format(it + 1, int(ans)))
