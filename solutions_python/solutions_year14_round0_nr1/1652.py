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
INPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Q1\A-small-attempt1.in"
OUTPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Q1\Out"

#====================================
#  MAIN FUNCTION
#====================================

def run(loadPath, outputPath):
    
    f = open(loadPath, "r")
    numCases = int(f.readline())

    output = ""

    for i in range(numCases):
        output += "Case #" + str(i+1) + ": "
        row1 = getLine(f)
        row2 = getLine(f)
        common = row1.intersection(row2)

        if len(common) == 1:
            output += str(common.pop())
        elif len(common) < 1:
            output += "Volunteer cheated!"
        else:
            output += "Bad magician!"

        output += "\n"

    fOut = open(outputPath, 'w')
    fOut.write(output)


def getLine(f):
    row = int(f.readline())
    grid = []
    for i in range(4):
        grid.append([int(x) for x in f.readline().split()]) # read all lines in
    return set(grid[row-1]) # return just the correct line as a set


run(INPUT_PATH, OUTPUT_PATH)