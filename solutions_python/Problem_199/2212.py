import math
import fractions

inFilePath =  'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\Q\\A-large.in'
outFilePath = 'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\Q\\A-large.out'
seperator = ' '

def parseFile(inFileName):
    inFile = open(inFileName)
    T = parseNum(inFile.readline())
    ProblemArr = []
    for k in range(T):
        string = inFile.readline()
        ProblemArr.append(ProblemSet(*string.split(' ')))
    inFile.close()
    return ProblemArr


class ProblemSet():
    def __init__(self,S,K):
        self.S = [i for i in S]
        self.K = int(K)

def solvePS(ps):
    S = ps.S
    K = ps.K
    count = 0
    for i in range(len(S)):
        if S[i] == '-':
            if (i + K) <= len(S):
                count += 1
                for j in range(K):
                    if S[i+j] == '-':
                        S[i+j] = '+'
                    else:
                        S[i+j] = '-'
            else:
                return 'IMPOSSIBLE'
    return count

    
   
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
