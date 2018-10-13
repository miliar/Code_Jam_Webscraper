#!/usr/bin/python2.6 -tt
import sys

def calculateCookies(inputFileName):
    inputFile = open(inputFileName, 'r')
    t = inputFile.readline()
    for i in range(int(t)):
        result = solveSet(inputFile)
        print "".join(['Case #', str(i + 1), ': ', "{0:.7f}".format(result)])

def solveSet(inputFile):
    set = inputFile.readline().rstrip().split(' ')
    c = float(set[0])
    f = float(set[1])
    x = float(set[2])
    totalTimeCurrent = 0
    totalTimePrevious = 0
    currentRate = 2
    while totalTimePrevious >= totalTimeCurrent:
        timeToNext = c / currentRate
        timeToTotal = x / currentRate
        if timeToTotal < timeToNext:
            return totalTimeCurrent + timeToTotal
        elif totalTimePrevious > 0 and totalTimeCurrent + timeToTotal >= totalTimePrevious:
            return totalTimePrevious
        else:
            totalTimePrevious = totalTimeCurrent + timeToTotal
            totalTimeCurrent = totalTimeCurrent + timeToNext
            currentRate += f
    return totalTimeCurrent


# Define a main() function that prints a greeting
def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: sys.argv[0]')
        sys.exit(1)
    inputFileName = sys.argv[1]
    calculateCookies(inputFileName)

# Standard boilerplate that calls the main function
if __name__ == '__main__':
    main()
