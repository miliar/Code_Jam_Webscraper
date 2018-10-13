#!/usr/bin/env python

def solve(C,F,X):
    spend = 0
    rate = 2
    step = 0
    while True:
        step = step + 1
        if X/rate > (C/rate + X/(rate+F)):
            # wait
            spend = spend + C/rate
            rate = rate + F
        else:
            spend = spend + X/rate
            break

    return spend

N = int(raw_input())
for t in range(N):
    input = map(float, raw_input().split())

    print 'Case #%d:' % (t+1) , 
    print round(solve(input[0], input[1], input[2]),7)


