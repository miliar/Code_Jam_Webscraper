#!/usr/bin/env python
import sys
import string

data = open(sys.argv[1],"r").readlines()
n = int(data[0])
data = data[1:]

def build_solve():
    text ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    solv ="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    m ={}
    for i in range(len(text)):
        if (text[i]!=' '):
            m[text[i]] = solv[i]

    s1=s2=''
    for x in m:
        s1+=x
        s2+=m[x]

    return s1,s2

s1,s2 = build_solve()
s1+="qz"
s2+="zq"

i = 1
for s in data:
    s = s.translate(string.maketrans(s1,s2)).strip()
    print "Case #%d: %s" %(i,s)
    i+=1
