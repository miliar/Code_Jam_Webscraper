#!#!\bin\python
#encoding UTF-8
#solution4.py

import string
import linecache

inname = "D-large.in"
outname = inname.rstrip(".in") + ".out"
fin = open(inname, "r")
fout = open(outname, "w")

allCaseNum = int(linecache.getline(inname, 1).rstrip("\n"))
caseNum = 0
blockNum = 0

def DeceitfulWar(naomi, ken, blockNum):
    naomi.sort()
    ken.sort()
    DeceitfulWarScore = 0
    while blockNum > 0:
        while naomi[blockNum-1] < ken[blockNum-1]:
            del naomi[0]
            del ken[blockNum-1]
            blockNum = len(naomi)
            if blockNum == 0:
                return DeceitfulWarScore
        del naomi[blockNum-1]
        del ken[blockNum-1]
        blockNum = len(naomi)
        DeceitfulWarScore = DeceitfulWarScore + 1
        if blockNum == 0:
            return DeceitfulWarScore

def OptimalWar(naomi, ken, blockNum):
    naomi.sort()
    ken.sort()
    OptimalWarScore = 0
    while blockNum > 0:
        j = 0
        while naomi[0] > ken[j]:
            j = j + 1
            if j >= blockNum:
                return (blockNum+OptimalWarScore)
        del naomi[0]
        del ken[j]
        blockNum = len(naomi)
    return OptimalWarScore


for caseNum in xrange(1, allCaseNum+1):
    blockNum = int(linecache.getline(inname, 3*caseNum-1).rstrip("\n"))
    naomi = linecache.getline(inname, 3*caseNum).rstrip("\n").split( )
    ken = linecache.getline(inname, 3*caseNum+1).rstrip("\n").split( )
    blockNum2 = blockNum
    naomi2 = [item[:] for item in naomi]
    ken2 = [item[:] for item in ken]
    DeceitfulWarScore = DeceitfulWar(naomi, ken, blockNum)
    OptimalWarScore = OptimalWar(naomi2, ken2, blockNum2)
    answer = "Case #%s: %s %s\n" %(caseNum, DeceitfulWarScore, OptimalWarScore)
    fout.write(answer)
fin.close()
fout.close()
