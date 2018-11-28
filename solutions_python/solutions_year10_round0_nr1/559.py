#!/usr/bin/env python

from __future__ import print_function
import sys
import math

with open(sys.argv[1], 'r') as input:
    with open(sys.argv[1] + ".out", 'w') as output:
        t = int(input.readline().strip())
        for case in range(0, t):
            params = input.readline().split()
            n, k = int(params[0]), int(params[1])
            
            result = "OFF"
            
            s = k - int(math.pow(2,n) - 1)
            if s >= 0 and s % int(math.pow(2,n)) == 0:
                result = "ON"
            
            output.write("Case #{0}: {1}\n".format(str(case+1), result))

