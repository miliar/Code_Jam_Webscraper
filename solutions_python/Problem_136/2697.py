#!/usr/bin/env python

def calc(c, f, x):
    cap, time = 2.0, 0.0
    while True:
        if x <= c:
            return time + x / cap
        elif (x - c) / cap < x / (cap + f): # don't buy
            return time + x / cap
        else: # buy
            time += c / cap
            cap += f

T = input()
for t in xrange(T):
    c, f, x = [float(i) for i in raw_input().split()]
    print('Case #{}: {:.7f}'.format(t + 1, calc(c, f, x)))
