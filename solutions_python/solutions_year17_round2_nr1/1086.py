#!/usr/bin/env python3
# Cruise Control

# from sys import argv

# global variables and constants
inData = []
TEST = False # not all caps

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

if TEST:
    pass

# problem-specific defs

# main

T = int(input())

for tt in range(1, T+1): # for each test case
    D, N = [int(x) for x in input().split()] # skip the explicit " "
    horses = []
    for nn in range(N):
        # position, max speed
        horses.append([int(x) for x in input().split()]) # Ki, Si
    # print(horses)

    # arrivals = [(D - horses[i][0])/horses[i][1] for i in range(len(horses))]
    # print(arrivals)
    arrivalTime = max([(D - horses[i][0])/horses[i][1] for i in
                       range(len(horses))])

    # arrivalTime = max(arrivals)

    speed = D/arrivalTime

    print('Case #' + str(tt) + ': %.6f' % speed)
