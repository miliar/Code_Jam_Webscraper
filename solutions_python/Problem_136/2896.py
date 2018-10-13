#!/usr/bin/env python

def get_min_time():
    C, F, X = map(float, raw_input().split())

    capacity = 2
    total_time = 0.0
    while total_time + (C / capacity) + (X / (capacity + F)) < total_time + (X / capacity):
        total_time += (C / capacity)
        capacity += F
    return total_time + (X / capacity) 

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        print 'Case #%d: %s' % (i + 1, get_min_time())
