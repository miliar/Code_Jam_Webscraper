#!/usr/bin/python
    
def hasBest(total, value, surprise):
    if value < 2:
        threshold = value
    else: 
        threshold = value * 3 - 2
        if(surprise):
            threshold = threshold - 2
    return total >= threshold

def myDebug(varName, varValue):
    print 'DEBUG ' + varName + ': ' + str(varValue)

def process(line):
    lineList = [int(x) for x in line.split()]

    noGooglers  = lineList[0]
    noSurprises = lineList[1]
    value       = lineList[2]
    
    #myDebug('noGooglers', noGooglers)
    #myDebug('noSurprises', noSurprises)
    #myDebug('value', value)
    
    totals = lineList[3:]

    assert(len(totals) == noGooglers)
    
    listOfNoSurprise = [x for x in totals if hasBest(x, value, False)]
   
    listOfCandidateSurprise = totals[:]
    
    for x in listOfNoSurprise:
        listOfCandidateSurprise.remove(x)

    listOfSurprise = [x for x in listOfCandidateSurprise if hasBest(x, value, True)]
    
    numOfCandidates = len(listOfNoSurprise) + min(len(listOfSurprise), noSurprises)
    return  numOfCandidates

def analyze(filename):
    f = open(filename)
    noLines = int(f.readline())

    count = 1
    for i in range (noLines):
        line = f.readline()

        print 'Case #{num}: '.format(num = count) + str(process(line))
        count = count + 1

analyze('input')
