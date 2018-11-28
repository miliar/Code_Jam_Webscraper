import math
from fractions import Fraction

inFilePath =  'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\1B\\A-large.in'
outFilePath = 'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\1B\\A-large.out'
seperator = ' '

def parseFile(inFileName):
    inFile = open(inFileName)
    T = parseNum(inFile.readline())
    ProblemArr = []
    for k in range(T):
        (D,N) = parseVec(inFile.readline())
        H = []
        for i in range(N):
            H.append(parseVec(inFile.readline()))
        ProblemArr.append(ProblemSet(D,N,H))
    inFile.close()
    return ProblemArr


class ProblemSet():
    def __init__(self,D,N,H):
        self.D = D
        self.N = N
        self.H = H

def solvePS(ps):
    times = [getTime(h[0],ps.D,h[1]) for h in ps.H]
    return float(ps.D/max(times))
        
def getTime(k,d,s):
    return Fraction(d-k,s)
    
   
def parseNum(line):
    return int(line)

def parseVec(line):
    vecValues = line.split(seperator)
    return [int(value) for value in vecValues]

def psOutFormat(iterNum,res):
    return 'Case #{0}: {1}\n'.format(iterNum+1,res)
        
def writeToFile(results,outFileStr):
    outFile = open(outFileStr,'w')
    try:
        resultArr = [psOutFormat(i,results[i]) for i in range(len(results))]
        outFile.writelines(resultArr)
    finally:
        outFile.close()
    
def solveProblemSet():
    ps = parseFile(inFilePath)
    results = []
    for i in range(len(ps)):
        results.append(solvePS(ps[i]))
    writeToFile(results,outFilePath)
    print('done!')


solveProblemSet()
#ps = ProblemSet([24,97,2])
#print(solvePS(ps))
