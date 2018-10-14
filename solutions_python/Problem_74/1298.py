#!/usr/bin/env python

import sys
import math

__author__ = 'cka3o4nik'


def make_robot_turns(s):
    turns = []
    for i in range(0, len(s), 2):
        turns.append(s[i])
    return turns


def separate_robot_mins(s):
    a = []
    b = []
    for i in range(0, len(s)):
        if s[i] == 'O':
            i += 1;
            a.append(s[i])
        elif s[i] == 'B':
            i += 1;
            b.append(s[i])
    return a, b

def calc_minutes(turns, buttons):
    robota, robotb = buttons[0], buttons[1]
    a_mins, b_mins = 0, 0
    a_prev_button, b_prev_button = 1, 1
    for turn in turns:
        if turn == 'O':
            a_button = int (robota.pop(0))
            a_mins += math.fabs(a_button - a_prev_button)
            if a_mins < b_mins:
                a_mins = b_mins
            a_mins += 1
            a_prev_button = a_button
        elif turn == 'B':
            b_button = int (robotb.pop(0))
            b_mins += math.fabs(b_button - b_prev_button)
            if b_mins < a_mins:
                b_mins = a_mins
            b_mins += 1
            b_prev_button = b_button
    if a_mins > b_mins:
        return a_mins
    else:
        return b_mins


line_num = int (sys.stdin.readline())
lines = []
for i in range(0, line_num):
    lines.append(sys.stdin.readline())
lines = [s.strip()[2:len(s)] for s in lines]
chars = []
for l in lines:
    chars.append(l.split())
for i in range(0, len(chars)):
    mins = calc_minutes(make_robot_turns(chars[i]), separate_robot_mins(chars[i]))
    print 'Case #%d: %d' % (i + 1, mins)

