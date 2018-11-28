#!/usr/bin/env python

import sys

def loadFile(filename):
    games = []
    no_games = 0
    with open(filename, 'r') as infile:
        no_games = int(infile.readline().strip())
        outputfilename = filename.split('.')[0] + '.out'
        with open(outputfilename, 'w') as outfile:
            for i in range(no_games):
                game = brdLineFromLine(infile.readline())
                
                s = getMinimumSeconds(game)
                outfile.write("Case #%d: %.7f\n"%(i+1, s))
                
def brdLineFromLine(line):
    return [float(a) for a in line.strip().split(' ')]

def getMinimumSeconds(game):

    C = game[0]
    F = game[1]
    X = game[2]
    # print C, F, X
    startRate = 2
    noFarms = 0
    totalTime = 0
    currentMoney = 0
    timeToComplete = X/startRate
    lastTime = timeToComplete + 1
    timeToNextFarm = C/startRate
    timeToCompleteWithNewFarm = (C /(startRate + F)) + timeToNextFarm
    # print timeToComplete, timeToNextFarm, timeToCompleteWithNewFarm
    while timeToComplete < lastTime:
        # print timeToComplete, timeToNextFarm, timeToCompleteWithNewFarm
        noFarms += 1
        totalTime = timeToNextFarm
        lastTime = timeToComplete
        timeToComplete = (X/(startRate + F*noFarms)) + totalTime
        timeToNextFarm = (C/(startRate + F*noFarms)) + totalTime
        timeToCompleteWithNewFarm = (C/(startRate + F*(noFarms+1))) + timeToNextFarm
        # print timeToComplete, timeToNextFarm, timeToCompleteWithNewFarm
        
    totalTime = lastTime
    # print totalTime
    return totalTime

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    loadFile(inputfilename)
    