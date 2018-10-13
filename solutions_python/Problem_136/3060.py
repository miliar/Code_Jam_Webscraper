#!/bin/python

import fileinput
import pdb

T = int(raw_input());
for i in range(T):
    [C, F, X] = map(float, raw_input().split())
    S = 2.0
    acc_time = 0
    time_to_win = X / S
    time_to_farm = (C / S)
    time_to_win_with_farm = time_to_farm + (X / (S + F))
    
    while time_to_win_with_farm < time_to_win:
        acc_time += time_to_farm
        S += F
        time_to_farm = (C / S)
        time_to_win = acc_time + (X / S)
        time_to_win_with_farm = acc_time + (C / S) + (X / (S + F))
        
    print 'Case #%d: %.7f' % (i+1, time_to_win)