#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = int(raw_input())

COOKIE_PER_SEC = 2.0

for i in xrange(T):
    FARM_COST, FARM_REVENUE, GOAL = map(float, raw_input().split(' '))
    t = 0.
    score = 0.
    farms = 0


    while score < GOAL:
        t_waiting = (GOAL - score) / (COOKIE_PER_SEC + farms * FARM_REVENUE)

        t_build_farm = (FARM_COST - score) / (COOKIE_PER_SEC + farms * FARM_REVENUE)
        t_farm = t_build_farm + GOAL / (COOKIE_PER_SEC + (farms + 1) * FARM_REVENUE)

        if t_farm < t_waiting:
            farms += 1
            dt = t_build_farm
            ds = 0
        else:
            dt = t_waiting
            ds = dt * (COOKIE_PER_SEC + farms * FARM_REVENUE)

        t += dt
        score += ds


    print 'Case #{0}: {1:.7f}'.format(i + 1, t)