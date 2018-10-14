#!/usr/local/bin/python
# Yen-Ming Lee <leeym@leeym.com>
# http://HOST/codejam/contest/dashboard?c=6254486#s=pA

import getopt
import math
import os
import re
import string
import sys

opt, arg = getopt.getopt(sys.argv[1:], 'vd')
verbose = False
debug = False
for k, v in opt:
    if k == '-v':
        verbose = True
    if k == '-d':
        debug = True

def digits(N):
    D = {}
    while N >= 1:
      	D[N % 10] = 1
	N /= 10
    return D

def solve(N):
    M = {}
    D = {}
    n = 0
    i = 0
    while True:
    	i = i + 1
	n = N * i
	if M.has_key(n):
	  return "INSOMNIA"
	M[n] = 1
	for d in digits(n):
	  D[d] = 1
	if len(D) == 10:
	  return n

T = int(sys.stdin.readline().rstrip())
for t in range(1, T+1):
    print >> sys.stderr, "Case #%d/%d" % (t, T)
    N = int(sys.stdin.readline().rstrip())
    print "Case #%d: %s" % (t, solve(N))
