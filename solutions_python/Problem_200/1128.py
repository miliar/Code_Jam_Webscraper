from math import *
from fractions import Fraction as F
import sys
import os

si = sys.stdin
so = sys.stdout
se = sys.stderr

readline = raw_input
readargs = lambda : readline().split()
readints = lambda : map(int, readargs())

T = readints()[0]

def tidy(x):
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            return False
    return True

def strict_tidy(x):
    for i in range(1, len(x)):
        if x[i] <= x[i - 1]:
            return False
    return True

for t in range(1, T + 1):
    n = readline().strip()
    print ('Case #%d:' % t),
    if tidy(n):
        print n
        continue
    pos = len(n)
    while pos and not strict_tidy(n[:pos]):
        pos -= 1
    if pos == 0:
        print '9' * (len(n) - 1)
    else:
        print (str(int(n[:pos]) - 1) + ('9' * (len(n) - pos))).lstrip('0')
