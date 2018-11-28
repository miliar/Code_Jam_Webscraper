#!/usr/bin/env python

import sys
import re

L,D,N = sys.stdin.next().strip().split()
L=int(L)
D=int(D)
N=int(N)
words = []
for i in range(D):
    row = sys.stdin.next().strip()
    words.append(row)

words = ' '.join(words)
for i in range(1,N+1):
    case = sys.stdin.next().strip()
    case = case.replace("(","[").replace(")","]")
    print "Case #%s: %s"%(i,len(re.findall(case,words)))
