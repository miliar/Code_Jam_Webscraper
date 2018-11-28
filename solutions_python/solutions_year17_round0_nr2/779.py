from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

dic = {}

def dig(n):

    if n == 0:
        return [0]

    ans = []

    while n > 0:
        ans.append(n % 10)
        n = n / 10

    ans.reverse()
    return ans

def sol(n):
    digits = dig(n)

    i = 0
    badFound = 0
    incl = 0
    rep = []
    lastNewValue = 0

    while (i + 1 < len(digits)):
        if (digits[i] != lastNewValue):
            lastNewValue = digits[i]
            lastI = i

        if (digits[i] > digits[i+1]):
            badFound = 1
            break

        i += 1

    i = 0
    if badFound == 0:
        return n

    while (i < len(digits)):
        if i < lastI:
            rep.append(digits[i])
        elif i == lastI:
            rep.append(digits[i] - 1)
        else:
            rep.append(9)
        i += 1

    ans = 0
    for d in rep:
        ans *= 10
        ans += d

    return ans

T = int(stdin.readline())

for i in range(1,T+1):

    n, = map(int, stdin.readline().split())
    
    print "Case #" + str(i) + ":", 
    print sol(n)
    
