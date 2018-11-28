#!/usr/bin/env python

import sys

def loadFile(filename):
    games = []
    no_games = 0
    with open(filename, 'r') as file:
        no_games = int(file.readline().strip())

        for i in range(no_games):
            ans1 = int(file.readline().strip())
            brd1 = []
            brd1.append(brdLineFromLine(file.readline()))
            brd1.append(brdLineFromLine(file.readline()))
            brd1.append(brdLineFromLine(file.readline()))
            brd1.append(brdLineFromLine(file.readline()))
            ans2 = int(file.readline().strip())
            brd2 = []
            brd2.append(brdLineFromLine(file.readline()))
            brd2.append(brdLineFromLine(file.readline()))
            brd2.append(brdLineFromLine(file.readline()))
            brd2.append(brdLineFromLine(file.readline()))
            games.append((ans1, brd1, ans2, brd2))
    return games

def brdLineFromLine(line):
    return [int(a) for a in line.strip().split(' ')]

def determineOutcome(game):
    choice1 = game[1][game[0]-1]
    choice2 = game[3][game[2]-1]
    possible = [a for a in choice1 if a in choice2]
    return possible
    
def saveOutcome(inputfilename, outcomes):
    outputfilename = inputfilename.split('.')[0] + '.out'
    with open(outputfilename, 'w') as file:
        i = 0
        for outcome in outcomes:
            i += 1
            if len(outcome) == 1:
                file.write("Case #%d: %d\n"%(i, outcome[0]))
            elif len(outcome) > 1:
                file.write("Case #%d: Bad magician!\n"%i)
            elif len(outcome) == 0:
                file.write("Case #%d: Volunteer cheated!\n"%i)

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    games = loadFile(inputfilename)
    outcomes = []
    for game in games:
        outcomes.append(determineOutcome(game))
    saveOutcome(inputfilename, outcomes)
    