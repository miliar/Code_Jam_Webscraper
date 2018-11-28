#!/usr/bin/python

import sys

def line():
    return sys.stdin.readline()[:-1]

if __name__ == '__main__':
    numberOfCases = int(line())
    for caseNumber in range(numberOfCases):
        position = dict()
        position['O'] = 1
        position['B'] = 1
        timeElapsed = 0
        spareTime = 0
        lastRobot = ''
        moves = line().split()
        N = int(moves[0])
        for i in range(N):
            robot = moves[2*i+1]
            button = int(moves[2*i+2])
            distanceToTravel = abs(position[robot] - button)
            if robot == lastRobot:
                thisTrip = distanceToTravel
                spareTime += thisTrip + 1
                timeElapsed += thisTrip + 1
            else:
                movedWhileWaiting = min(distanceToTravel,spareTime)
                remainingMoves = abs(distanceToTravel - movedWhileWaiting)
                spareTime = remainingMoves + 1
                timeElapsed += remainingMoves + 1
                lastRobot = robot
            position[robot] = button
        print "Case #" + str(caseNumber+1) + ": " + str(timeElapsed)
