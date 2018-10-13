#!/usr/bin/env python

import sys
f = sys.stdin
def readline(): return f.readline().strip()
def readlines(n): return [readline() for _ in xrange(n)]
def readintlines(n): return [readints() for _ in xrange(n)]
def readsplit(): return readline().split()
def readint(): return int(readline())
def readints(): return map(int, readsplit())
def readfloat(): return float(readline())
def readfloats(): return map(float, readsplit())

T = readint()

def case(n):
    cost, rate_inc, win = readfloats()
    rate = 2
    time = 0

    while True:
        time_to_win = win / rate
        time_with_farm = win / (rate+rate_inc)
        time_to_farm = cost / rate

        if time_to_win < time_to_farm + time_with_farm:
            time += time_to_win
            break
        else:
            time += time_to_farm
            rate += rate_inc

    print 'Case #%i: %.7f' % (n, time)

if __name__ == '__main__':
    for n in xrange(1, T+1):
        case(n)
