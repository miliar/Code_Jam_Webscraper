#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from itertools import permutations
from collections import Counter, defaultdict

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        t = int(input())
        for i in range(t):
            n, k = map(int, input().split())
            cakes = reversed(sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: x[0]))
            # print(cakes)
            ans = 0
            for elem in permutations(cakes, k):
                # print(elem)
                s = elem[0][0] ** 2
                for e in elem:
                    s += 2 * e[0] * e[1]
                # print(s)
                ans = max(s, ans)
            # print(ans)
            pi = ans * math.pi
            print("Case #{0}: {1}".format(i+1, pi))
            
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
