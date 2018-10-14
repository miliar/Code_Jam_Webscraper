# usr/bin python
#-*- coding:utf-8 -*-

import re

words,pat =[],[]
for i,line in enumerate(open(r"D:\pgz\py\A-large.in")):
    if i == 0:
        l,d,n = [int(l) for l in line.strip().split()]
    elif i > 0 and i <= d:
        words += [line.strip()]
    elif i > d:
        pat += [line.strip()]

f = open(r"D:\pgz\py\output.txt","w")
for i in range(n):
    p = pat[i].replace("(","[").replace(")","]")
    r = re.compile(p)
    count = 0
    for j in range(d):
        mo = r.match(words[j])
        if mo:
            count += 1
    f.write("Case #%(num)d: %(count)d\n"%{"num":i+1,"count":count})

f.close()