#!/bin/env python
from math import sqrt

T = int(input())
# compute all squares from 1 to 1000
squares = set([i*i for i in range(1, 32)])

def check_condition(x):
    s = str(x)
    if not s==s[::-1]:
        return False
    if x in squares:
        sqx = int(sqrt(x))
        s = str(sqx)
        return s==s[::-1]
    return False

for i in range(T):
    s = input()
    s = s.split(" ")
    A, B = int(s[0]), int(s[1])
    cnt = 0 ;
    for x in range(A, B+1):
        if check_condition(x):
            cnt += 1
    print("Case #%d: %d"%(i+1, cnt))
