#!/usr/bin/python

import math

with open('input.txt', 'r') as inp:
    cases = int(inp.readline())
    case_no = 1

    for case in inp:

        C, F, X = [float(l.strip()) for l in case.split(' ')]
        
        speed   = 2
        seconds = 0

        while True:

            seconds_to_farm = C / speed
            seconds_to_win  = X / speed
            next_seconds_to_win = X / (speed + F)

            if seconds_to_farm + next_seconds_to_win > seconds_to_win:
                seconds += seconds_to_win
                break
            else:
                seconds += seconds_to_farm
                speed += F

        print 'Case #%d: %.7f' % (case_no, seconds)

        case_no += 1
