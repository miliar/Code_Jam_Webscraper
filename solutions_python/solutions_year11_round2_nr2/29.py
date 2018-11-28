#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

from __future__ import division
from __future__ import print_function

import sys


class HotDog(object):
    def __init__(self, index, P, V):
        self.index = index
        self.pos = P
        self.qty = V

        self.left = P
        self.right = P
        self.size = 0

        self.time = 0
        self.max_time = 0

    @property
    def center(self):
        return (self.left + self.right)/2

    def spread(self):
        #print("({0}, {1}) begin spread, qty={2}, time={3}".format(
        #    self.left, self.right, self.qty, self.time
        #))
        newsize = D * (self.qty-1)
        #self.time += (newsize - self.size)/2
        self.size = newsize

        newleft = self.center - self.size/2
        newright = self.center + self.size/2

        extra_time = max(abs(self.left-newleft), abs(self.right-newright))
        self.time += extra_time

        self.left = newleft
        self.right = newright

        self.max_time = max(self.time, self.max_time)

        #print("({0}, {1}) end spread, qty={2}, time={3}".format(
        #    self.left, self.right, self.qty, self.time
        #))

    def avoid(self, other):
        intersection = self.right + D - other.left
        #print("({0}, {1}) avoid ({2}, {3}), intersection={4}".format(
        #    self.left, self.right, other.left, other.right, intersection
        #))
        if intersection <= 0:
            other.max_time = max(self.max_time, other.max_time)
            return 0 # No join needed

        else:
            delta_time = abs(self.time - other.time)
            if delta_time > 10**(-6):
                delta_offset = min(delta_time, intersection)
                if self.time < other.time:
                    self.time += delta_offset
                    self.left -= delta_offset
                    self.right -= delta_offset
                elif self.time > other.time:
                    other.time += delta_offset
                    other.left += delta_offset
                    other.right += delta_offset

                return 1 # Try avoiding again
            else:
                # Let's join!
                self.max_time = max(self.max_time, other.max_time)
                self.time = max(self.time, other.time)
                self.qty += other.qty
                self.left = min(self.left, other.left)
                self.right = max(self.right, other.right)
                self.spread()
                return 2 # Join performed, must kill the 'other'


def run_testcase():
    global D

    C, D = [int(x) for x in raw_input().split()]
    v = [
        HotDog(i, *[int(x) for x in raw_input().split()] )
        for i in range(C)
    ]

    for dog in v:
        dog.spread()

    cont = True
    while cont:
        cont = False
        for i in range(len(v)-1):
            ret = v[i].avoid(v[i+1])
            if ret == 1:
                ret = v[i].avoid(v[i+1])
                cont = True

            if ret == 2:
                cont = True
                v.pop(i+1)

            if ret > 0:
                break

    return max(dog.time for dog in v)


max_testcases = int(raw_input().strip())
for T in range(1, max_testcases+1):
    print("Case #{0}: {1:f}".format(T, run_testcase()))
