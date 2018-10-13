import os
import sys
from sys import setrecursionlimit
import time
import math
import collections
import heapq

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'C-small-attempt0.in'))
sys.stdout = open('out3.txt', 'wb')

cases = int(raw_input())

def is_palindromic(n):
    return str(n) == str(n)[::-1]



#@memoized
def d(n, r):
    if n == 0:
        return r
    else:
        return d(math.floor(n / 10), r * 10 + (n % 10))

setrecursionlimit(1000000000)


def f(x, y):
    if x > 0:
        return f(x - 2 * y - 1, y + 1)
    else:
        return pow(0, -x)

palindromes = set()
for i in range(1, 10000):
    if not is_palindromic(i): continue
    if f(i, 0) * (1 if d(i, 0) == i else 0) == 1 and is_palindromic(int(math.sqrt(i))):
        palindromes.add(i)


for case in range(cases):
    A, B = raw_input().split(' ')
    A = int(A)
    B = int(B)

    cnt = 0
    for i in range(A, B+1):
        if i in palindromes:
            cnt += 1
    print 'Case #%d: %d' % (case + 1, cnt)