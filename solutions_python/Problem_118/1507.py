import os
import sys
from math import *

f = open('input.txt', 'r')

t = f.readline()

def is_palindrome(a):
    return str(a) == str(a)[::-1]

s = {0: 0}
c = 0

for i in range(1, 10000002):
    if is_palindrome(i) and is_palindrome(i*i):
        c += 1
    s[i] = c


for zt in range(int(t)):
    lo, hi = f.readline().split(' ')

    lo = int(ceil(sqrt(int(lo))) + 0.5)
    hi = int(floor(sqrt(int(hi))) + 0.5)

    print 'Case #%d: %d' % (zt+1, (s[hi] - s[lo-1]))
