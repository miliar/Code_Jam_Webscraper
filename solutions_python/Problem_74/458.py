#!/usr/bin/env python

from sys import stdin
#from math import abs

lines = stdin.readlines()
T = int(lines[0])
lines = lines[1:]
for t in range(0,T):
    split = lines[t].split()
    N = int(split[0])
    queue = split[1:]
    result = 0 # time needed for the first n button presses
    pos = {True: 1, False:1}  # position of the robots
    store = {True:0, False:0} # time in store for the robots to move
    prev = None # last active robot

    for n in range(0, N):
        # get action
        robot  = queue[2*n] == 'B'
        button = int(queue[2*n+1])
        # distance to cover
        move = abs(button - pos[robot]) 
        # time needed to move and press button
        time = max(move - store[robot], 0) + 1
        # move robot, press button and accumulate time
        result += time
        pos[robot] = button
        # press of a button invalidates time in store for movement
        store[robot] = 0
        # add to time in store for other
        store[not robot] += time
         
        prev = robot

    print("Case #{0}: {1}".format(t+1, result))
    
