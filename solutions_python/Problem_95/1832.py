#!/usr/bin/python

import os

import sys


str1 ="""
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
str2 ="""
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""


d = {}

for i in range(len(str1)):
    d[str1[i]] = str2[i]

d["z"]="q"
d["q"]="z"

print sorted(str2)

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
fh_o = open("out.txt","w")
for i in range(T):
    case = fh.readline().strip()
    print >> fh_o, "Case #"+str(i+1)+": "+"".join(map(lambda x: d[x], case))

fh_o.close()
fh.close()
