#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def is_tidy(n):
    """
    Check if an integer is ``tidy``
    """
    return sorted(n) == list(n)

def down(i):
    """
    cycling number
    """
    return i-1 if i else 9

def main():
    """
    Do the job.
    """
    t = int(sys.stdin.readline())
    for i in range(t):
        n = map(int, sys.stdin.readline().strip('\n'))
        b = is_tidy(n)
        count = 0
        while not b:
            n[-(count+1)] = 9
            n[-(count+2)] -= 1
            b = is_tidy(n)
            count += 1
        print("Case #%s: %s" %(i+1, int("".join(map(str,n)))))
main()
