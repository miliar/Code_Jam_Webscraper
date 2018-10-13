#!/usr/bin/env python

N = input()

for _ in range(N):
        C, F, X = map(float, raw_input().split())

        speed = 2.0
        time = 0.0

        while True:
                newtime = time + C / speed + X / (speed + F)
                if newtime < time + X / speed:
                        time += C / speed
                        speed += F
                else:
                        break

        print 'Case #%d: %.7f' % (_ + 1, time + X / speed)