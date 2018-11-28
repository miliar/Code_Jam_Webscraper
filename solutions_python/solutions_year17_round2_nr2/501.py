import math
import fractions
inFilePath =  'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\1B\\B-small.in'
outFilePath = 'C:\\Users\\Orr\\Desktop\\CodeJam\\2017\\1B\\B-small.out'
seperator = ' '

def parseFile(inFileName):
    inFile = open(inFileName)
    T = parseNum(inFile.readline())
    ProblemArr = []
    for k in range(T):
        ProblemArr.append(ProblemSet(*parseVec(inFile.readline())))
    inFile.close()
    return ProblemArr


class ProblemSet():
    def __init__(self,N,R,O,Y,G,B,V):
        self.N = N
        self.R = R
        self.O = O
        self.Y = Y
        self.G = G
        self.B = B
        self.V = V

def solvePS(ps):
    colors = [('R',ps.R),('B',ps.B),('Y',ps.Y),('G',ps.G),('O',ps.O),('V',ps.V)]
    colors.sort(key = lambda x:x[1],reverse = True)
    if colors[0][1] + colors[1][1] == ps.N:
        if colors[0][1] == colors[1][1] and match(colors[0][0],colors[1][0]):
            return ''.join([colors[1][0] if i % 2 == 1 else colors[0][0] for i in range(ps.N)])
        else:
            return 'IMPOSSIBLE'
    single = oneColor(ps.N,ps.R-ps.G,ps.B-ps.O,ps.Y-ps.V)
    if single == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'
    mul = []
    for i in range(len(single)-1,-1,-1):
        mul.append(single[i])
        if single[i] == 'R' and ps.G > 0:
            mul.append('G')
            mul.append('R')
            ps.G -=1
        if single[i] == 'B' and ps.O > 0:
            mul.append('O')
            mul.append('B')
            ps.O -=1
        if single[i] == 'Y' and ps.V > 0:
            mul.append('V')
            mul.append('Y')
            ps.V -=1
    return ''.join(mul)

def match(a,b):
    c = [a,b]
    for i in range(2):
        if c[i] == 'G':
            c[i] = 'BY'
        if c[i] == 'O':
            c[i] = 'RY'
        if c[i] == 'V':
            c[i] = 'BR'
    for char in c[0]:
        if char in c[1]:
            return False
    return True

def oneColor(N,R,B,Y):
    colors = [('R',R),('B',B),('Y',Y)]
    colors.sort(key = lambda x:x[1],reverse = True)
    if min([colors[0][1],colors[1][1],colors[2][1]]) < 0:
        return 'IMPOSSIBLE'
    if colors[0][1] > colors[1][1] + colors[2][1]:
        return 'IMPOSSIBLE'
    else:
        two = [colors[1][0] if (i % 2 == 1 and (i-1) < 2*colors[1][1]) else colors[0][0] for i in range(colors[0][1]+colors[1][1])]
        if colors[2][1] > 0:
            leastColor = colors[2][1]
            output = []
            for i in range(colors[0][1]+colors[1][1]-1,-1,-1):
                if leastColor > 0:
                    output.append(colors[2][0])
                    leastColor -=1
                output.append(two[i])
        else:
            output = two
        return output
            

def twoColor(ps):
    1==1  
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
