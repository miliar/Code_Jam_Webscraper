#!/usr/bin/env python

def timebase(input):
    """docstring for timebase"""
    #print input
    i = 1
    maps = {}
    for j in range(len(input)):
        if input[j] not in maps:
            maps[input[j]] = i
            if i == 1:
                i = 0
            elif i == 0:
                i = 2
            else:
                i += 1
    sum = 0
    base = len(maps.keys())
    if base == 1:
        base += 1
    for j in range(len(input)):
        sum += base ** (len(input) - j - 1) * maps[input[j]]
    return sum
