#!/usr/bin/python

def solve(count, *rawButtons):
    buttons = zip(rawButtons[::2], map(int, rawButtons[1::2]))

    time = 1
    spacetimes = {'B': (1, 1), 'O': (1, 1)}

    for robot, destination in buttons:
        start, startTime = spacetimes[robot]
        time = max(startTime + abs(destination - start) , time) + 1
        spacetimes[robot] = destination, time

    return time - 1



T = int(raw_input())
for i in range(T):
    print "Case #%i: %i" % (i+1, solve(*(raw_input().split(' '))))

