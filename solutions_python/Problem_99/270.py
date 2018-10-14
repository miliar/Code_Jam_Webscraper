#!/bin/env python

from __future__ import print_function

def correctStrokes(A, B, seqNum):
    return 2*(A-seqNum)+(B-A+1)

def errorStrokes(A, B, seqNum):
    return 2*(A-seqNum)+(2*B-A+2)

def calcE(prevProbCorrect,
          currProbCorrect,
          correctStrokes,
          errorStrokes):
    probAllSoFarCorrect = prevProbCorrect*currProbCorrect
    probOtherwise = 1.0-probAllSoFarCorrect
    return (probAllSoFarCorrect*correctStrokes + \
        probOtherwise*errorStrokes,
            probAllSoFarCorrect)
            

def confidentE(A, B, probCorrect): # This is the product
    # of all probs
    return probCorrect*(B-A+1)+((1-probCorrect)*(2*B-A+2))

def despondentE(A, B):
    return B+2

def writeCase(theFile, caseNumber, answer):
    theLine = "Case #%d: %s"%(caseNumber, answer)
    theFile.write(theLine + "\n")
    return

def solveCase(theFile):
    AandB = theFile.readline().strip().split()
    A = int(AandB[0])
    B = int(AandB[1])
    probs = [float(x) for x in theFile.readline().strip().split()]
    probAllCorrect = reduce(lambda x,y:x*y, probs)
    result = min((confidentE(A, B, probAllCorrect), despondentE(A, B)))
    counter = 1
    prevProb = 1.0
    # print(probs)
    for prob in probs[:-1]:
        theCorrectStrokes = correctStrokes(A, B, counter)
        theErrorStrokes = errorStrokes(A, B, counter)
        candidate, prevProb = calcE(prevProb, prob, theCorrectStrokes, theErrorStrokes)
        # print(candidate, prevProb)
        if candidate < result:
            result = candidate
        counter += 1
    return result

        
                


def main(fileName):
    f = open(fileName, "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(f))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])
