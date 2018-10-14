#!/bin/python
# -*- coding: utf-8 -*



f1 = open("input.txt", 'r')
f2 = open("output.txt", 'w')
t = int(f1.readline())
n = 1
while t:
    c, f, x = [float(a) for a in f1.readline().split()]
    
    results = {} # pour un nombre d'achats donné
    
    while(True):
        farms = len(results)
        rate = 2
        cookie = 0
        time = 0
        while farms :
            time += c / rate
            cookie -= c
            rate += f
            farms -= 1
        total = x/rate + time
        if len(results) and total > min(results.values()):
            break
        results[len(results)]= total
    
    answer = results[len(results)-1]
    f2.write("Case #{}: {}\n".format(n, answer))
    
    n += 1 
    t -= 1
    
f1.close()
f2.close()

