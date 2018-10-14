#!/usr/bin/python
import re

"""
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
"""

def find(s, k):
    try:
        p=s.index("1")
        return p
    except:
        return -1

def invert(s, p, n):
    l=list(s)
    if (p+n)>len(s):
        p=len(s)-n
    for i in range(n):
        if l[i+p]=="0":
            l[i+p]="1"
        else:
            l[i+p]="0"
    return "".join(l)

def solver(s, k):

    m=0
    l=list(s)
    if "1" not in s:
        return m
    elif k>len(s):
        return -1
    else:
        while int("".join(l))>0 and m<=len(l):
            p=find(l,k)
            if p>=0:
                l=list(invert("".join(l), p, k))
                m += 1
            else:
                m+=1

        if int("".join(l))==0:
            return m
        else:
            return -1

case=1
aresults=[]
fout=open("result.txt", "wb+")
cases = open("data.txt", "rb").readlines()[1:]
for line in cases:
    s, k=line.strip().split(" ")
    s=re.sub("\+", "0", s)
    s=re.sub("\-", "1", s)
    flips=solver(s, int(k))
    if flips<0:
        flips="IMPOSSIBLE"
    else:
        flips="%d" % flips
    reslt="Case #%d: %s" % (case, flips)
    aresults.append(reslt)
    case+=1
fout.write("\n".join(aresults))
fout.close()
