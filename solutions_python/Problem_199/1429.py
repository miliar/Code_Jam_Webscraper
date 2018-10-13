# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:12:49 2017

@author: David
"""

def reverse(s):
    res = ''
    for i in range(len(s)):
        if s[i] == '+':
            res += '-'
        elif s[i] == '-':
            res += '+'
    return res


def calcFunction(inp, K):
    result = 0
    for i in range(len(inp)):
        if inp[i]=='-':
            if i > len(inp)-K:
                return "IMPOSSIBLE"
            inp = inp[:i] + reverse(inp[i:i+K]) + inp[i+K:]
            result += 1
    return result;


out = open('output.txt', 'w')
t = int(input())
for el in range(1, t+1):
    inp, K = input().split(' ')
    K = int(K)
    result = calcFunction(inp, K)
    print("Case #" + str(el) + ": " + str(result))
    out.write("Case #" + str(el) + ": " + str(result) + "\n")
out.close()