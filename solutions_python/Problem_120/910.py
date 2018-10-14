#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, itertools, re, sys
import fileinput as f
from collections import Counter
from functools import wraps
 
def memo(func):
    """docstring for memo"""
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def get_req(r,k):
    return ((r+k)+(r+k-1))*((r+k)-(r+k-1))

def gen_seq(r,t):
    n = 2*r+1
    while True:
        yield 4*n - 1
        n+=1 

def main():
    """docstring for main"""
    f = open(sys.argv[1])
    T = int(f.readline())
    for i in range(T):
        r, t = map(int, f.readline().strip().split())
        count = 0
        k = 1
        while t >= 0:
            req = get_req(r,k)
            if req > t:
                break
            t -= req
            count+=1
            k+=2
        print "Case #%d: %s" % (i + 1, count)

if __name__ == '__main__':
    main()
