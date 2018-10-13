import sys
import os
import shutil
import csv
import math as m
import re

#====================================
#  CONSTANTS
#====================================
# file structure related
INPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Deceiptful War\D-large.in"
OUTPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Deceiptful War\Out"

# verbose flag
# v = True
v = False

#====================================
#  MAIN FUNCTION
#====================================


def run(loadPath, outputPath):
    f = open(loadPath, "r")
    numCases = int(f.readline())

    output = ""

    for i in range(numCases):
        solution = solve(f)
        output += "Case #" + str(i + 1) + ": " + str(solution[0]) + " " + str(solution[1])
        output += "\n"

    fOut = open(outputPath, 'w')
    fOut.write(output)

def solve(f):
    rounds = int(f.readline())
    nSorted = sorted([float(x) for x in f.readline().split()])
    kSorted = sorted([float(x) for x in f.readline().split()])
    nSortedClone = nSorted[:]
    kSortedClone = kSorted[:]

    numCheatingWins = solveGame(nSorted, kSorted, rounds, True)
    numWins = solveGame(nSortedClone, kSortedClone, rounds, False)

    return numCheatingWins, numWins

def solveGame(nSorted, kSorted, rounds, cheating):
    nWins = 0
    for r in range(rounds):
        print
        smallestN = nSorted.pop(0)
        smallestK = kSorted[0]
        
        if cheating:
            if smallestN > smallestK:
                moveN = (smallestN, 0.9999999999)
            else:
                moveN = (smallestN, kSorted[-1]-0.000001)
        else:
            if smallestN > smallestK:
                #       (actual, tells)
                moveN = (smallestN, smallestN)
            else:
                moveN = (smallestN, smallestN)

        biggestK = kSorted[-1]
        if moveN[1] > biggestK:
            moveK = kSorted.pop(0)
        else:
            popK = 0
            breakLoop = False
            for x in range(len(kSorted)):
                if not breakLoop:
                    if kSorted[x] > moveN[1]:
                        popK = x
                        breakLoop = True
            moveK = kSorted.pop(popK)
        if moveN[0]>moveK: nWins += 1
        # print "%s. N(%s) %s K(%s)" %(r, moveN, {True: ">", False:"<"}[moveN>moveK], moveK)
    return nWins


run(INPUT_PATH, OUTPUT_PATH)