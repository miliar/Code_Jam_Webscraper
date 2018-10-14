# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 16:20:10 2017

@author: sanindra
"""

def replace(s):
    m=''
    for i in s: m += '-' if i=='+' else '+'
    return m

t = input()

for i in xrange(t):
    s, n= raw_input().split()
    c, a, b, n = 0, 0, 0, int(n)
    cond = True
    while s.count('-')>=n or cond:
        cond = False if s.count('-')<n else True 
        for j in xrange(len(s)):
            if s[j] == '-':
                a+=1
            elif s[j]=='+' and a!=0:
                b+=1
            if a+b == n:
                c+=1
                s = s[:j-(n-1)] + replace(s[j-(n-1):j+1]) +s[j+1:]
                a, b = 0, 0
                break
    if s.count('-') != 0:
        c = 'IMPOSSIBLE'
    else:
        c = str(c)
    print "Case #{}: {}".format(i+1,c)