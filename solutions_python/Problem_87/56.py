#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

from __future__ import division
from __future__ import print_function

import string
import sys


class Section(object):
    def __init__(self, speed, length):
        self.speed = speed
        self.length = length

    def time(self):
        return self.length / self.speed

    def try_run(self, remaining_time):
        global run_bonus

        run_speed = self.speed + run_bonus
        run_time = self.length / run_speed

        if run_time <= remaining_time:
            self.speed = run_speed
            return (remaining_time-run_time, None)
        else:
            run_length = remaining_time * run_speed
            s = Section(self.speed, self.length - run_length)

            self.speed = run_speed
            self.length = run_length
            return (0, s)

    def __repr__(self):
        return '<{0}m @ {1}m/s>'.format(self.length, self.speed)


def run_testcase():
    X, S, R, t, N = [int(x.strip()) for x in raw_input().strip().split()]
    walkways = [
        # B_i, E_i, w_i
        [int(x.strip()) for x in raw_input().strip().split()]
        for i in range(N)
    ]

    global run_bonus
    run_bonus = R-S

    # Splitting the long corridor into sections
    sections = []
    begin = 0
    for w in walkways:
        if begin < w[0]:
            sections.append(Section(S, w[0]-begin))
        sections.append(Section(S+w[2], w[1]-w[0]))
        begin = w[1]
    if begin < X:
        sections.append(Section(S, X-begin))
    del begin

    # Sort sections by speed
    sections.sort(key=lambda x: x.speed)

    # Running at the slowest sections
    running_time = t
    total_time = 0
    for s in sections:
        if running_time < 10**-6:
            total_time += s.time()
        else:
            running_time, new_section = s.try_run(running_time)
            total_time += s.time()
            if new_section is not None:
                total_time += new_section.time()

    return total_time


max_testcases = int(raw_input().strip())
for T in range(1, max_testcases+1):
    print("Case #{0}: {1}".format(T, run_testcase()))
