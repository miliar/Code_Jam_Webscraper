#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Google Code Jam template

from __future__ import print_function, division, absolute_import, unicode_literals
import collections
import time
import sys
import os
import random
import numpy as np
import scipy as sp
import networkx as nx
from numba import jit
import heapq

def tidy(N):
    s = str(N)
    last = int(s[0])
    for c in s[1:]:
        if int(c)<last:
            return False
        last = int(c)
    return True

def solve(N):
    save = 1
    for i in range(1,N+1):
        if tidy(i):
            save = i
    return save

T = int(sys.stdin.readline())
for t in range(1,T+1):
    N = int(sys.stdin.readline())
    solution = "%s" % solve(N)
    print("Case #%i: %s" % (t,solution))
