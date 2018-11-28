import sys


def GetDataPerLine(f):
    line = f.readline()
    mapOfLine = line.split(" ")
    K = int(mapOfLine[1])
    S = mapOfLine[0]

    S_Int = [0] * len(S)
    
    for i in range(0, len(S)):
        if (S[i] == '-'):
            S_Int[i] = 0
        else:
            S_Int[i] = 1
    
    return [K, S_Int]

def SolveQuestionPerTest(listOfInput):
    [K,S] = listOfInput

    counter = 0

    maxIndexToRun = len(S) - K + 1
    
    for i in range (0, maxIndexToRun):
        # flip K from this location
        if (S[i] is 0):
            counter = counter + 1
            for flipIndex in range (i, i+K):
                S[flipIndex] = 1- S[flipIndex]

    #print (S)
                    
    for i in range(0, len(S)):
        if (S[i] == 0):
            return 'IMPOSSIBLE'
        
    return str(counter)    
                
    
Output = []
f = open('A-large.in')
out = open ('output.txt', 'w')
T = int(f.readline())
print ('T = ' + str(T))
for i in range(0,T):
    strSolution = SolveQuestionPerTest ( GetDataPerLine(f) )
    strCase = 'Case #' + str(i+1) + ': ' + strSolution + '\n'
    #print (strCase)
    out.write(strCase)

out.close()
