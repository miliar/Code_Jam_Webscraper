from __future__ import print_function

def solveProblem(initialState):
    print(initialState)
    result = []

    for r in range(len(initialState)):
        letterIndex = -1
        # for each row find first letter
        for c in range(len(initialState[r])):
            if initialState[r][c] == '?':
                continue
            for rewrite in range(letterIndex+1, c):
                initialState[r][rewrite] = initialState[r][c]
            letterIndex = c
        if not letterIndex == -1:
            for fill in range(letterIndex, len(initialState[r])):
                initialState[r][fill] = initialState[r][letterIndex]
        #if the whole row is empty and not top row
        if letterIndex == -1 and not r == 0:
            for d in range(len(initialState[r])):
                initialState[r][d] = initialState[r-1][d]
            print(initialState[r][c])

    #loop through again
    for r in range(len(initialState)-1, -1, -1):
        letterIndex = -1
        # for each row find first letter
        for c in range(len(initialState[r])):
            if initialState[r][c] == '?':
                continue
            for rewrite in range(letterIndex+1, c):
                initialState[r][rewrite] = initialState[r][c]
            letterIndex = c
        if not letterIndex == -1:
            for fill in range(letterIndex, len(initialState[r])):
                initialState[r][fill] = initialState[r][letterIndex]
        #if the whole row is empty and not top row
        if letterIndex == -1:
            for d in range(len(initialState[r])):
                initialState[r][d] = initialState[r+1][d]
            print(initialState[r][c])
    return "", initialState

import sys

def main():
    inPath = sys.argv[1]
    outPath = inPath.split('.')[0] + '.out'
    file = open(inPath, "r")
    out = open(outPath, "w")
    rows = 0
    cols = 0
    initialState = []
    currentCase = 0
    caseRead = 0
    #Read Input File
    for line in file:
        #Skip first line
        if currentCase == 0:
            currentCase += 1
            continue
        #Get the input
        inputs = line.split(' ')
        if len(inputs) == 2:
            #must be case definition
            rows = int(inputs[0])
            cols = int(inputs[1])
            caseRead = 0
            initialState = []
        if len(inputs) == 1:
            initialState.append(list(line.strip()))
            caseRead += 1
        if caseRead == rows:
            print("Solving Case: " + str(currentCase))
            header, results = solveProblem(initialState)
            #format header
            headerStr = ""
            for r in header:
                headerStr += str(r) + ' '
            print('Case #{case}: {headerStr}'.format(case=currentCase, headerStr=headerStr), file=out)

            #format the rest of the results
            for result in results:
                print(''.join(result), file=out)

            currentCase += 1

if __name__ == "__main__":
    main()