#!/usr/bin/python

import math

def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n / 10, partial * 10 + n % 10)

TestCasesStr = raw_input()
TestCases = int(TestCasesStr)

for t in range(1,TestCases+1):
    lst = map(int, raw_input().split())

    A = lst[0]
    B = lst[1]

    a = int(math.ceil(math.sqrt(A)))
    b = int(math.sqrt(B))

    #print "a = {0} b = {1} A = {2} B = {3}".format(a,b,A,B)

    count = 0;

    for i in range(a,b+1):
        if i == ReverseNumber(i):
            i2 = i*i;
            if i2 == ReverseNumber(i2):
                count = count + 1;

    print "Case #{0}: {1}".format(t , count)

