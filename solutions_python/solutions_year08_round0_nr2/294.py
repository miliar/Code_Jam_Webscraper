#!/usr/bin/env python
# -*- coding: utf-8 -*-

def timeToMin(str):
    l = str.split(":")
    return int(l[0])*60 + int(l[1])          

def minToTime(minutes):
    hour = minutes / 60
    if hour < 10:
        hour = "0" + str(hour)
        
    minutes2 = minutes % 60
    if minutes2 < 10:
        minutes2 = "0" + str(minutes2)
    return str(hour) + ":" + str(minutes2)

def resolve (t, na, nb, va, vb):
    oa = 0
    ob = 0

    atual_a = 0
    atual_b = 0

    for i in range(24*60):
        #print "%s - %d %d, %d %d" % (minToTime(i), oa, ob, atual_a, atual_b)
        
        #check if there are buses getting in A
        for bus_a in va:
            if bus_a[1]+t == i:
                atual_b += 1
             
        #check if there are buses getting in B
        for bus_b in vb:
            if bus_b[1]+t == i:
                atual_a += 1
             
        #check if there are buses leaving A
        for bus_a in va:
            if bus_a[0] == i:
                if atual_a == 0:
                    oa += 1
                else:
                    atual_a -= 1
            
        #check if there are buses leaving B
        for bus_b in vb:
            if bus_b[0] == i:
                if atual_b == 0:
                    ob += 1
                else:
                    atual_b -= 1
    
    return (oa, ob)

def compara(x1,x2):
    return x1[0] - x2[0];

def train():
    n = input()

    for i in range(n):
        t = input()
        na,nb = raw_input().split(' ')
        na = int(na)
        nb = int(nb)
        
        va = []
        for j in range(na):
            h1,h2 = raw_input().split(' ')
            va.append((timeToMin(h1), timeToMin(h2)))
        va.sort(compara)
        #print va

        vb = []
        for j in range(nb):
            h1,h2 = raw_input().split(' ')
            vb.append((timeToMin(h1), timeToMin(h2)))
        vb.sort(compara)
        #print vb

        s = resolve(t, na, nb, va, vb)  
        print "Case #%d: %d %d" % (i+1, s[0],s[1])
if __name__ == "__main__":
    train()
