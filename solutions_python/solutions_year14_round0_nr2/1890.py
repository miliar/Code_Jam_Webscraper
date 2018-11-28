#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def greedy(target, productivity, farm_price, farm_productivity):

    if productivity >= target:
        return target / productivity

    return min(target / productivity, greedy(target, productivity + farm_productivity, farm_price, farm_productivity) + farm_price / productivity)

T = input()

for t in xrange(T):

    C, F, X = [float(x) for x in raw_input().split()]

    target = X
    productivity = 2.0
    farm_price = C
    farm_productivity = F
    last_time = target / productivity
    time_sum = 0

    while True:

        time_sum += farm_price / productivity
        productivity += farm_productivity

        next_time = target / productivity + time_sum

        if next_time > last_time:
            break
        last_time = next_time

    print "Case #{0}: {1:.7f}".format(t + 1, last_time)

