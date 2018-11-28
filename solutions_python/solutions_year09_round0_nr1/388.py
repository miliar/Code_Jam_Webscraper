#!/usr/bin/python
import sys

def read_tokens(f):
  for line in f:
          for t in line.split():
                    yield t

words = []
tokenNumber = 0
caseNumber = 1

for token in read_tokens(sys.stdin):
    if (tokenNumber == 0):
        intL = int(token)
    elif (tokenNumber == 1):
        intD = int(token)
    elif (tokenNumber == 2):
        intN = int(token)
    elif (tokenNumber <= intD + 2):
        words.append(token)
    else:
        stubs = [""]

        chars = []
        inmulti = False

        for j in range(0, len(token)):
            myChar = token [j]
            if (myChar == "("):
                chars = []
                inmulti = True
            elif (myChar == ")"):
                tempStubs = []
                for preStubs in stubs:
                    for multiChar in chars:
                        candidateWord = preStubs + multiChar
                        cWordLen = len(candidateWord)
                        for realWord in words:
                            if (realWord.count(candidateWord, 0, cWordLen) == 1):
                                tempStubs.append(candidateWord)
                                break

                stubs = tempStubs
            elif (inmulti):
                chars.append(myChar)
            else:
                tempStubs = []
                for preStubs in stubs:
                    candidateWord = preStubs + myChar
                    cWordLen = len(candidateWord)
                    for realWord in words:
                        if (realWord.count(candidateWord, 0, cWordLen) == 1):
                            tempStubs.append(candidateWord)
                            break

                stubs = tempStubs

        count = 0
        for possibleWord in stubs:
            if possibleWord in words: 
                count = count + 1

        # print "Case #%d: %d" % caseNumber, count
        print "Case #" + str(caseNumber) + ": " + str(count)
        caseNumber = caseNumber + 1
    tokenNumber = tokenNumber + 1
