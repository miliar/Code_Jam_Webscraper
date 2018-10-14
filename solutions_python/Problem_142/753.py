#!/usr/bin/env python

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys

# <codecell>

def loadFile(filename):
    games = []
    no_games = 0
    with open(filename, 'r') as infile:
        no_games = int(infile.readline().strip())
        outputfilename = filename.split('.')[0] + '.out'
        with open(outputfilename, 'w') as outfile:
            for i in range(int(no_games)):
                no_strings = infile.readline().strip()
                strings = []
                for j in range(int(no_strings)):
                    strings.append(infile.readline().strip())
                s = getScore(strings)
                if s >= 0:
                    outfile.write("Case #%d: %d\n"%(i+1, s))
                else:
                    print strings
                    outfile.write("Case #%d: Fegla Won\n"%(i+1))

# <codecell>

def getScore(strings):
    no_strings = len(strings)
    letterOrder = []
    representations = []
    avgs = []
    for string in strings:
        repres = defaultForm(string)
        if len(letterOrder) == 0:
            letterOrder = getLetterOrder(repres)

        else:
            newLetterOrder = getLetterOrder(repres)
            if (len(newLetterOrder) != len(letterOrder)):
                print "unequal"
                return -1
            if not checkLetterOrders(letterOrder, newLetterOrder):
                return -1
        avgs.append(getCounts(repres))
        representations.append(repres)
    sc = getScores(avgs)
    if sc < 0:
        print strings
    return getScores(avgs)

# <codecell>

def defaultForm(string):
    result = []
    for char in string:

        if len(result) == 0 or result[-1][0] != char:
            result.append((char, 1))
        else:
            result[-1] = (char, result[-1][1] + 1)
    return result

# <codecell>

def getLetterOrder(rep):
    order = []
    for tup in rep:
        order.append(tup[0])
    return order

# <codecell>

def checkLetterOrders(rep1, rep2):
    try:
        tups = zip(rep1, rep2)

    except:
        return False
    for tup in tups:
        if tup[0] != tup[1]:
            return False
    return True

# <codecell>

def getCounts(rep):
    order = []
    for tup in rep:
        order.append(tup[1])
    return order

# <codecell>

def getScores(avgs):
    # if len(avgs) => 2:
        totals = [0 for i in range(len(avgs[0]))]
        counts = len(avgs)
        for i in range(len(avgs)):
            for j in range(len(avgs[i])):
                try:
                    totals[j] += avgs[i][j]
                except:
                    print avgs
                    return -1
        aaaa = []
        for a in totals:
            aaaa.append(a/counts)
        totalScore = 0
        for a in avgs:
            for i in range(len(a)):
                totalScore += abs(a[i] - aaaa[i])
        return totalScore
    # else:
    #     for i in range(len(avgs)):
            
# <codecell>

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    loadFile(inputfilename)

# <codecell>


