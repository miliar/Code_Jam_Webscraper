#!/bin/python

TT = int(input())

for ntc in range(1,TT+1):

    C,F,X = [float(i) for i in input().split()]

    cF = 2.0

    total = 0
    while( True ):
        r = X / cF
        rpf = C / cF + X / (F + cF)

        if( r < rpf ):
            total += r
            break

        total += C/cF
        cF += F

    print("Case #%d: %.7f"%(ntc, total))
