# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:52:21 2017

@author: David
"""


def calcFunction(num):
    p=18
    c=0
    tidy = True
    for i in range(len(str(num))):
        digit = int(str(num)[i])
        if digit > c:
            p = i
            c = digit
        if digit < c:
            tidy = False
            break
    if tidy:
        return num
    result = str(num)[:p] + str(int(str(num)[p])-1) + '9'*(len(str(num))-p-1)
    result = int(result)
    return result


out = open('output.txt', 'w')
t = int(input())
for el in range(1, t+1):
    num = int(input())
    result = calcFunction(num)
    print("Case #" + str(el) + ": " + str(result))
    out.write("Case #" + str(el) + ": " + str(result) + "\n")
out.close()
