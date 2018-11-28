#!/usr/bin/env python

import re
import os
import sys
import time
from copy import copy
from itertools import *

try:
    import psyco
    psyco.full()
except:
    pass

def readint():
    return int(raw_input())

def readfloat():
    return float(raw_input())

def readlinearray(function):
    return map(function, raw_input().split())

def snapper(N, K):
    minimum = 2**N - 1
    current = K - minimum
    if current < 0:
        return False
    if (current % (2**N)) == 0:
        return True
    return False

def main():
    T = readint()
    for count in range(T):
        N, K = readlinearray(int)
        print 'Case #' + str(count + 1) + ':',
        if snapper(N, K):
            print 'ON'
        else:
            print 'OFF'

if __name__ == '__main__':
    main()

