# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:35:20 2014

@author: jatin
"""

f = open("input.txt","r")
fo = open("output.txt","w")
l = f.readlines()
tc = int(l[0])
for i in range(tc):
    s = "Case #" + str(i + 1) + ": "
    C,F,X = tuple([float(x) for x in l[i  + 1].split(" ")])
    S = 0.0
    Sf = []
    Sc = 0.0 
    Sa = 0.0
    Fm = 2.0
    # find out the time if not farm is bought
    while(1):
        Sf.append(S + X / Fm)
        S = S + C / Fm
        if min(Sf) < S:
            Sa = min(Sf)
            break
        Fm = Fm + F
    s = s + str(Sa)        
    if i + 1 < tc:
        s = s + '\n'
    fo.write(s)
fo.close()
f.close()