# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
def replace(i,string,char):
    return string[:i]+char+string[i+1:]

for t in range(1,int(input())+1):
    n=int(input())
    s=str(n)
    m=len(s)
    for i in range(len(s)-1):
        if int(s[m-i-2])>int(s[m-i-1]):
            s=s[:m-i-1]+"9"*(i+1)
            s=s[:m-i-2]+str(int(s[m-i-2])-1)+s[m-i-1:]
    if s[0]!="0":print("Case #{0}: {1}".format(t,s))
    else:print("Case #{0}: {1}".format(t,s[1:]))