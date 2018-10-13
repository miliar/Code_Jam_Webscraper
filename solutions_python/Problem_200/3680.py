# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 

@author: Watson123
"""

def tidy(s):
    n = len(s)
    ans = []
    for i in range(0,n):
        ans.append(int(s[i]))
    for i in reversed(range(0,n-1)):
        if ans[i] > ans[i+1]:
            ans[i] -= 1
            for j in range(i+1,n):
                ans[j] = 9
    s = ''
    for x in ans:
        s += str(x)
    if s[0] == '0':
        s = s[1:n]
    return s
  
#f = open("test.txt")         
f = open("B-large.in.txt")
inp = []
for line in f:
    for word in line.split():
        inp.append(word)
f.close()

ans = []
n = int(inp[0])
for s in inp[1:(n+1)]:
    ans.append(tidy(s))

# write answer
#f = open("test.out.txt", "w")   
f = open("B-large.out.txt", "w")  
i = 0
for x in ans:
    i += 1
    f.write("Case #" + str(i) + ": " + str(x) + "\n")
f.close()
    