#!/bin/env python



T = int(raw_input())

for i in range(T):
    CFX = [float(x) for x in raw_input().split()]
    C, F, X = CFX[0], CFX[1], CFX[2]

    cps = 2.0
    time = 0.0
    while (((X / (cps + F)) + (C / cps)) <
           (X / cps)):
        time += C / cps
        cps += F
    time += X / cps
    print("Case #{0}: {1:.7f}".format(i+1, time))
        
        
                 
