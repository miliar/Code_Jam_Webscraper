#!/usr/bin/env python
import sys

def readline():
    return sys.stdin.readline()

def readreal():
    return float(readline())

def readreals():
    return [float(x) for x in readline().strip().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().strip().split()]

def time_to_farm(C, rate):
    return C / rate

def time_to_goal(X, rate):
    return X / rate

def time_to_goal_with_new_farm(C, F, X, rate):
    return C / rate + X / (rate + F)

def read_case():
    C, F, X = readreals()
    rate = 2.0
    time = 0.0
    farm_time = time_to_goal_with_new_farm(C, F, X, rate)
    no_farm_time = X / rate
    while farm_time < no_farm_time:
        time += time_to_farm(C, rate)
        rate += F
        farm_time = time_to_goal_with_new_farm(C, F, X, rate)
        no_farm_time = X / rate
    time += no_farm_time
    return '{0:.7f}'.format(time)

def main():
    cases = readint()
    for c in range(1, cases + 1):
        print 'Case #{0:d}: {1}'.format(c, read_case())

if __name__ == '__main__':
    main()

