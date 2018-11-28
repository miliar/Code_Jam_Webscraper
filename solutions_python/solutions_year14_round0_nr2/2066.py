
import string, os, time, sys

# C = Cost per farm
# F = Added production per farm
# X = Goal (cookies)
def FindResult(C, F, X):

    currentProduction = 2.0;  # cookies per second
    currentBestRemaining = X / currentProduction
    elapsedTime = 0
    while True:
        if currentBestRemaining < (C / currentProduction):
            return currentBestRemaining + elapsedTime

        # What if we were to save up and buy another farm...
        whatifElapsedTime = elapsedTime + (C / currentProduction)
        whatifProduction = currentProduction + F
        whatifBestRemaining = X / whatifProduction

        if (elapsedTime + currentBestRemaining <
            whatifElapsedTime + whatifBestRemaining):
            return elapsedTime + currentBestRemaining

        elapsedTime = whatifElapsedTime
        currentProduction = whatifProduction
        currentBestRemaining = whatifBestRemaining
    

def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n").split(' ')
    C = float(caseline[0]) # Cost per farm
    F = float(caseline[1]) # Added production per farm
    X = float(caseline[2]) # Goal (cookies)

    result = FindResult(C, F, X)

    header = "Case #%(count)d: %(r).7f" % {"count":caseIndex, "r":result}
    print header


inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

