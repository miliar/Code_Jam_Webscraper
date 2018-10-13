import math
import fractions

inFilePath =  'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\Q\\B-large.in'
outFilePath = 'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\Q\\B-large.out'
seperator = ' '

def parseFile(inFileName):
    inFile = open(inFileName)
    T = parseNum(inFile.readline())
    ProblemArr = []
    for k in range(T):
        string = inFile.readline()
        ProblemArr.append(ProblemSet([int(i) for i in string if i != '\n']))
    inFile.close()
    return ProblemArr


class ProblemSet():
    def __init__(self,string):
        self.s = string
def solvePS(ps):
    s = ps.s
    lastStrInc,last = 0,0
    for i in range(len(s)):
        if last < s[i]:
            lastStrInc = i
        if last > s[i]:
            s[lastStrInc] -= 1
            for j in range(lastStrInc+1,len(s)):
                s[j] = 9
            break
        last = s[i]
    return int(''.join([str(i) for i in s]))

    
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
