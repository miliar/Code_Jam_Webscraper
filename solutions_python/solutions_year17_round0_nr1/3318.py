# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 

@author: Watson123
"""

import math

def flip(s, k, b):
    n = len(s)
    if b + k -1 >= n:
        return "Error!"
    else:
        ans = ""
        for i in range(0,n):
            if i in range(b,b + k):
                if s[i] == '-':             
                    ans += '+'
                else:                    
                    ans +='-' 
            else:
                ans += s[i] 
    return ans
 
def trimPluses(s):
    # remove +'s from front and back of string s
    n = len(s)
    i = 0
    while s[i] == '+' and i < n-1:
        i += 1
    j = n-1
    while s[j] == '+' and j > 0:
        j -= 1
    return s[i:(j+1)]
    
def flipsNo(s, k):
    n = len(s)
    if s == '':
        return 0
    if k > n:
        if s == n*'+':
            return 0
        else:
            return math.inf
    if s[0] == '-':
        s = flip(s,k,0)
        s = trimPluses(s)
        return 1 + flipsNo(s, k)
    else:
        s = trimPluses(s)
        return flipsNo(s, k)
    
f = open("A-small-attempt2.in.txt")
inp = []
for line in f:
    ln = []
    for word in line.split():
        ln.append(word)
    if ln != []:    
        inp.append(ln)
f.close()

ans = []
n = int(inp[0][0])
for i in range(1, n+1):
    ans.append(flipsNo(inp[i][0], int(inp[i][1])))

# write answer
f = open("A-small-attempt2.out.txt", "w")
i = 0
for x in ans:
    i += 1
    if x == math.inf:
        x = 'IMPOSSIBLE'
    f.write("Case #" + str(i) + ": " + str(x) + "\n")
f.close()
    