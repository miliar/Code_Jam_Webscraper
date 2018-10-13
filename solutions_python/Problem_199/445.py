#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat Apr 08 21:15:19 2017 +0800
# $Author: jiakai <jia.kai66@gmail.com>

import numpy as np
def work():
    line, k = input().split()
    k = int(k)
    line = np.array(list(map(['-', '+'].index, line)))


    ans = 0
    for i in range(0, len(line) - k + 1):
        if not line[i]:
            ans += 1
            line[i:i+k] ^= 1

    if sum(line) == len(line):
        return ans
    return 'IMPOSSIBLE'

def main():
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, work()))

if __name__ == '__main__':
    main()
