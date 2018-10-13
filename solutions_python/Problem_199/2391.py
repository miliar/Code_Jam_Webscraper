#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        t = int(input())
        for num in range(1, t + 1):
            s, k_str = input().split()
            k = int(k_str)
            l = [1 if e == '+' else 0 for e in s]
            ans = 0
            flg = True
            for index, e in enumerate(l):
                if e == 0:
                    if index + k - 1 >= len(l):
                        flg = False
                        break
                    else:
                        for j in range(index, index + k):
                            if l[j] == 0:
                                l[j] = 1
                            else:
                                l[j] = 0
                        ans += 1
            if flg:
                print("Case #{0}: {1}".format(num, ans))
            else:
                print("Case #{0}: IMPOSSIBLE".format(num))

        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
