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
            n = list(input())
            n_list_r = list(reversed(n))
            # print(n_list_r)
            for index in range(len(n_list_r) - 1):
                if int(n_list_r[index+1]) > int(n_list_r[index]):
                    for i in range(index + 1):
                        n_list_r[i] = '9'
                    n_list_r[index+1] = str(int(n_list_r[index+1]) - 1)
            # print(n_list_r)
            ans = ''
            flg = False
            for elem in reversed(n_list_r):
                if elem != '0':
                    flg = True
                if flg:
                    ans += str(elem)
            print("Case #{0}: {1}".format(num, ans))
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
