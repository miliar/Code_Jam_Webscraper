#!/bin/python3

import sys

def tidy(n):
    l = len(n)
    if l == 1:
        return n
    out_n = n
    if n == '10':
        return '9'
    first = int(n[0])
    for i in range(1, l):
        second = int(n[i])
        if first > second:
            out_n = n[:i-1] + str(first-1) + (l - i)*'9'
            break
        first = second
    if out_n[0] == '0':
        out_n = out_n[1:]
    return out_n
    
t = int(input().strip())
for a0 in range(t):
    number = input().strip()
    n1 = ""
    n2 = tidy(number)
    i = 0
    while n1 != n2:
        i += 1
        if i >= 20:
            break
        n1 = n2
        n2 = tidy(n1)
    print("Case #" + str(a0+1) + ": " + n2)