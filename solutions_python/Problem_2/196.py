#!/usr/bin/env python

import logging
import heapq

#INPUT_FILENAME = "B-small-attempt0.in"
INPUT_FILENAME = "B-large.in"

def parseMinutes(strTime):
    hours, minutes = strTime.split(":")
    return int(hours) * 60 + int(minutes)

def readInput(input):
    turnaroundMinutes = int(input.readline())
    numA, numB = [int(a) for a in input.readline().split()]
    trips = []
    type = 0
    for i in range(numA + numB):
        if i >= numA:
            type = 1
        departure, arrival = input.readline().split()
        departure = parseMinutes(departure)
        arrival = parseMinutes(arrival) + turnaroundMinutes
        trips.append((departure, arrival, type))
    trips.sort()
    return trips

def popNumPassed(minutes, arrivals):
    passed = 0
    while len(arrivals) > 0 and arrivals[0] <= minutes:
        heapq.heappop(arrivals)
        passed += 1
    return passed

def calc(trips):
    at = [0, 0]
    startedAt = [0, 0]
    running = [[], []]
    for trip in trips:
        minutes = trip[0]
        # note switched indexes
        at[1] += popNumPassed(minutes, running[0])
        at[0] += popNumPassed(minutes, running[1])

        type = trip[2]
        if at[type] == 0:
            startedAt[type] += 1
        else:
            at[type] -= 1
        heapq.heappush(running[type], trip[1])

    return startedAt

def main():
    input = file(INPUT_FILENAME)
    numCases = int(input.readline())
    for i in range(numCases):
        trips = readInput(input)
        atA, atB = calc(trips)
        print "Case #%s: %s %s" % (i + 1, atA, atB)

if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

