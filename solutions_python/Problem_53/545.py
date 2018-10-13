#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import sys
rdl = sys.stdin.readline
 
def process(case):
    """precessing case #"""
    n, k = (int(i) for i in rdl().split())
    a = 2**n - 1
    return 'ON' if k%(a+1)==a else 'OFF'
     
cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)