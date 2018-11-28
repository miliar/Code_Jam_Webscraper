# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 14:48:46 2017

@author: sandeep
"""

def tidy(x):
    
    s = str(x)
    for i in xrange(0, len(s) - 1):
        if int(s[i]) <= int(s[i+1]):
            continue
        else:
            return False
    return True
  
def check(x):
    
    for i in xrange(x , 0 , -1):
        if tidy(i):
            return i
        else:
            continue
    return 0

x = []
t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())  # read a list of integers, 2 in this case
    x.append(n)
    

for i in xrange(0,len(x)):
    p = check(x[i])
    print "Case #{}: {}".format(i + 1, p)

    