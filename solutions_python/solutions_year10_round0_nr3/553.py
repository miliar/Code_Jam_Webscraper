#!/usr/bin/env python

from __future__ import print_function
from collections import deque
import sys
import math

with open(sys.argv[1], 'r') as input:
    with open(sys.argv[1] + ".out", 'w') as output:
        t = int(input.readline().strip())
        
        for case in range(0, t):
            params = input.readline().split()
            r, k, n = int(params[0]), int(params[1]), int(params[2])
            
            groups = [int(g) for g in input.readline().split()]
            
            result = 0
            for i in range(0,r):
                train = []
                remaining = []
                num = 0
                for j in range(0,len(groups)):
                    if num + groups[j] <= k:
                        train.append(groups[j])
                        num += groups[j]
                    else:
                        remaining = groups[j:]
                        break
                
                result += num
                remaining.extend(train)
                groups = remaining
            
            output.write("Case #{0}: {1}\n".format(str(case+1), result))