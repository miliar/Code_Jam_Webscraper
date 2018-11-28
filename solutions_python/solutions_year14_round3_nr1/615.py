#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in input().split()]
def readint(): return int(input().strip())

debug = lambda x: None

def is_int(n):
    return int(n) == n

T = readint()
for i in range(T):
    num, denom = [int(e) for e in input().split('/')]
    debug(num)
    debug(denom)
    if not is_int((num * (2**40)) / denom):
        debug('True')
        print('Case #{0}: {1}'.format(i + 1, 'impossible'))
    else:
        debug('False')
        print('Case #{0}: {1}'.format(i + 1, math.ceil(math.log(denom / num, 2))))
