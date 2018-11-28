import os, sys


def readProblem(filename, numDataParts):
    #print filename
    fh = open(filename)
    numCases = int(fh.readline().strip())

    allCases = []
    for i in range(numCases):
        allCases.append([])
        for j in range(numDataParts):
            allCases[i].append([])
            numData = int(fh.readline().strip())
            for k in range(numData):
                allCases[i][j].append(fh.readline().strip())

    return allCases

def findLongestSuccessfulSpan(names, list):
    longLen = 0
    #print list
    for n in names:
        #print "trying name: %s" % (n)
        for i in range(len(list)):
            if list[i] == n:
                #print "list[%d] == n" % (i)
                if i > longLen:
                    longLen = i
                break
        else:
            return len(list)
    return longLen

def main(args):
    cases = readProblem(args[0], 2)
    for i in range(len(cases)):
        names = cases[i][0]
        queries = cases[i][1]
        currentSpan = 0
        numSwitches = 0
        while True:
            currentSpan += findLongestSuccessfulSpan(names, queries[currentSpan:])
            if currentSpan >= len(queries):
                break
            numSwitches += 1

        print "Case #%d: %d" % (i+1, numSwitches)

if __name__ == "__main__":
    main(sys.argv[1:])

