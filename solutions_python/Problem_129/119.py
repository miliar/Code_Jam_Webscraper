import re
import math

totalCases = 0
caseNumber = 0
name = "A-small-attempt0"
#name = 'test'

modulo = 1000002013

caseL = 0

inFile = file("%s.in" % name,"r")
outFile = open("%s.out" % name, "w")
lineNumber = 0

N = 0
M = 0

ml = []
originalPrice = 0

def price(stations):
    return N*stations - (stations*stations-stations)/2

def fillData(start, fin, p):
    ml[start-1] += p
    ml[fin-1] -= p

def determineSwappedPrice():
    total = 0
    ml.reverse()
    for i in range(len(ml)):
        start = i
        if ml[i] == 0:
            continue
        if ml[i] > 0:
            for j in range(i, -1, -1):
                if ml[j] < 0:
                    nj = -ml[j]
                    c = min(nj, ml[i])
                    thisp = price(abs(j-i))*c
                    total += thisp
                    #print thisp
                    total = total % modulo
                    ml[j] += c
                    ml[i] -= c
                    if ml[i] == 0:
                        break
    return total

for line in inFile:
    if (lineNumber == 0):
        # first line input
        row = str(line).strip().split()
        totalCases = int(row[0])
        caseNumber = 1
    else:
        row = str(line).strip().split()
        if M == 0:
            N = int(row[0])
            M = int(row[1])
            ml = [0]*N
            originalPrice = 0
        else:
            M-=1
            O = int(row[0])
            E = int(row[1])
            P = int(row[2])
            #print O, E, P
            originalPrice += price(E-O)*P
            if originalPrice > 1000002013:
                originalPrice = originalPrice % modulo
            fillData(O, E, P)



            if M == 0:
                #print ml
                
                swapPrice = determineSwappedPrice()
                outcome = originalPrice - swapPrice

                outcome = outcome % modulo

                caseOutput = "Case #%d: %d\n" % (caseNumber, outcome)
                
                #print caseOutput
                outFile.write(caseOutput)

                caseNumber += 1

    lineNumber+=1
    
inFile.close()
outFile.close()

print 'complete'



