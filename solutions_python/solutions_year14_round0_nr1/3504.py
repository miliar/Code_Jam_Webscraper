# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:03:20 2014

@author: jatin
"""

f = open("input.txt","r")
fo = open("output.txt","w")
l = f.readlines()
tc = int(l[0])
for i in range(tc):
    ans = int(l[i*10 + 1])
    ansrow = [int(x) for x in l[i*10 + 1 + ans].split(" ")]
    nextans = int(l[i*10 + 6])
    nextansrow = [int(x) for x in l[i*10 + 6 + nextans].split(" ")]
    sol = list(set(ansrow) & set(nextansrow))
    s = "Case #" + str(i + 1) + ": "
    if len(sol) == 1:
        s = s + str(sol[0])
    elif len(sol) == 0:
        s = s + "Volunteer cheated!"
    else:
        s = s + "Bad magician!"
    if i + 1 < tc:
        s = s + '\n'
    fo.write(s)
fo.close()
f.close()