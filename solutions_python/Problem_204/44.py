import os, sys, math, time;
startTime = time.time()

# Writes answers for each case to terminal and to output file.
def writeAnswer(outputFile, case, answer):
    line = 'Case #%s: %s' % (case + 1, answer)
    print line
    outputFile.write(line + "\n")

def solveAllCases(fileName):
    print 'Running problem ' + fileName
    inputFile = open(fileName + '.in', 'r')
    outputFile = open(fileName + '.out', 'w')
    cases = int(inputFile.readline())
    print str(cases) + ' cases'
    for case in range(cases):
        # print (time.time() - startTime)
        print 'Solving case ' + str(case + 1)
        writeAnswer(outputFile, case, solveCase(inputFile))

def listToString(list):
    return ', '.join(str(x) for x in list)

def solveCase(inputFile):
    answer = '?'
    line = inputFile.readline().split()
    # Each entry is how many grams to make one serving
    ingredients = [int(s) for s in inputFile.readline().split()]
    print 'Ingredients: ' + listToString(ingredients)
    packages = [[] for i in range(len(ingredients))]
    for i in range(len(ingredients)):
        packages[i] = sorted([float(s) for s in inputFile.readline().split()])
        print 'packages for %s: %s' % (i, listToString(packages[i]))

    readIndexes = [0 for i in range(len(ingredients))]
    numberOfPackages = 0;
    safety = 0
    while (True and safety < 1000):
        safety += 1
        smallestIngredient = 0
        smallestValue = 10000000
        largestValue = 0
        i = 0
        while i < len(readIndexes):
            if readIndexes[i] >= len(packages[i]):
                return numberOfPackages
            floatPackages = packages[i][readIndexes[i]] / ingredients[i]
            # print "%s, %s : %s" % (i, readIndexes[i], floatPackages)
            intPackages = round(floatPackages)
            if (floatPackages > 1.1 * intPackages or floatPackages < .9 * intPackages):
                # print "%s is invalid, retrying " % floatPackages
                readIndexes[i] += 1
                continue
            largestValue = max(largestValue, floatPackages)
            if floatPackages < smallestValue:
                smallestIngredient = i
                smallestValue = floatPackages
            i += 1

        # print "%s <= %s" % (smallestValue, largestValue)
        # print "%s >= %s" % (smallestValue *  1.1, .9 * largestValue)
        if smallestValue <= largestValue and smallestValue *  1.1 >= .9 * largestValue:
            numberOfPackages += 1
            for i in range(len(readIndexes)):
                readIndexes[i] += 1
            continue

        readIndexes[smallestIngredient] += 1

    print "Exceeded safety bounds"


    # Read input and solve case here, then return the answer.
    return '?'

solveAllCases('B-large')
