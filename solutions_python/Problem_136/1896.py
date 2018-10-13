#!/usr/bin/python
#coding: utf-8

t = int(raw_input())

for case in xrange(1,t+1):
    i = [eval (n) for n in raw_input().strip().split(" ")]
    c,f,x = float(i[0]),float(i[1]),float(i[2])
    tempsTotal = 0.
    cps = 2.
    while (True):
        tempsNecessaire = c / cps
        if (tempsNecessaire + (x / (cps+f)) < x / cps):
            cps += f
            tempsTotal += tempsNecessaire
        else:
            tempsTotal += x / cps
            break
    print "Case #%d: %f" % (case,tempsTotal)
