#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-
#
# © 2014 Peter Volkov (pva)


C = 500.                                                                          
F = 4.                                                                            
X = 2000.                                                                         
V = 2. 

with open("B-large.in", "r") as f:
    lines = f.readlines()

N = int(lines[0])
n = 0
while n < N:
    (C, F, X) = lines[n+1].split()
    (C, F, X) = (float(C), float(F), float(X))
    #print(C, F, X)
    n += 1

    T0 = X/V
    #print("0: T = %s" % (T0))
    i = 1
    Tb = C/V
    T = Tb + X/(V+F)
    #print("1: T = %s" % (T))
    while T0 > T:
        i += 1
        T0 = T
        Tb += C/(V+(i-1)*F)
        T = Tb + X/(V+i*F)
        #print("%s: T = %s" % (i, T))

    print("Case #%s: %s" % (n, T0))


