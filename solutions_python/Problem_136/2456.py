#!/usr/bin/python
# vi: set fileencoding=utf-8 :

import math

def minimum_seconds(C, F, X): 
    setup_time = 0.0
    best_time = X / 2.0
    factory_number = 0
    while True:
        setup_time += C / (2.0 + factory_number * F)
        factory_number += 1
        new_time = setup_time + X / (2.0 + factory_number * F)
        if new_time < best_time:
            best_time = new_time
        if best_time < setup_time:
            break
    return round(best_time, 7)


T = int(raw_input())
for t in range(T):
    line = raw_input()
    C, F, X = line.split(' ')
    C = float(C)
    F = float(F)
    X = float(X)
    print 'Case #' + str(t + 1) + ':', minimum_seconds(C, F, X)
