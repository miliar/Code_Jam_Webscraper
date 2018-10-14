import sys

cache = set()

from math import sqrt, ceil

def isPalindrome(x):
    y = str(x)
    return y == y[::-1]

def isValid(x):
    y = str(x)
    if len(y) > 1:
        for d in y:
            if int(d) > 2:
                return False
    return isPalindrome(x)

def solve():
    A, B = 1, 10**100
    a = int(ceil(sqrt(A)))
    b = int(sqrt(B))
    count = 0
    n = a
    while n <= b:
        if n in cache:
            count += 1
        elif isValid(n) and isPalindrome(n*n):
            count += 1
            cache.add(n)
        n += 1
    return str(count)

solve()

scache = sorted(list(cache))

c_out = open('cache.txt', 'w')
for c in scache:
    c_out.write(str(c) + ' ')

c_out.close()
