def readFile(fileName):
    f = open(fileName)
    caseList = []
    lineNum = 0
    for line in f:
        lineNum += 1
        content = line.split()
        if lineNum == 1:
            print content[0],'test cases are read.'
        elif lineNum % 2 == 0:
            L = int(content[0])
            X = int(content[1])
        else:
            caseList.append((L,X,content[0]))
    f.close()
    return caseList

##qResult = [['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k'],
##         ['i', '-1', 'k', '-j', '-i', '1', '-k', 'j'],
##         ['j', '-k', '-1', 'i', '-j', 'k', '1', '-i'],
##         ['k', 'j', '-i', '-1', '-k', '-j', 'i', '1'],
##         ['-1', '-i', '-j', '-k', '1', 'i', 'j', 'k'],
##         ['-i', '1', '-k', 'j', 'i', '-1', 'k', '-j'],
##         ['-j', 'k', '1', '-i', 'j', '-k', '-1', 'i'],
##         ['-k', '-j', 'i', '1', 'k', 'j', '-i', '-1']]
##list1 = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']

def product(l1,l2,qResult,list1):
    return qResult[list1.index(l1)][list1.index(l2)]


def equalIJK(case, qResult, list1):
    L = case[0]
    X = case[1]
    while X > 11:
        X -= 4
    base = case[2]*X

    indexI = 0
    l1 = base[indexI]
    indexI += 1
    while l1 != 'i' and indexI < min(L*4,len(base)-2):
        l2 = base[indexI]
        l1 = product(l1, l2, qResult, list1)
        indexI += 1
    if l1 != 'i':
        return 'NO'

    indexJ = indexI
    l1 = base[indexJ]
    indexJ += 1
    while l1 != 'j' and indexJ < min(indexI+L*4, len(base)-1):
        l2 = base[indexJ]
        l1 = product(l1, l2, qResult, list1)
        indexJ += 1
    if l1 != 'j':
        return 'NO'

    limit = len(base)-indexJ
    while limit > L*4:
        limit -= L*4
    l1 = base[indexJ]
    for indexK in range(indexJ+1,indexJ+limit):
        l2 = base[indexK]
        l1 = product(l1, l2, qResult, list1)
    if l1 != 'k':
        return 'NO'
    else:
        return 'YES'
    

def solveIt(caseList, qResult, list1):
    output = ''
    for j in range(len(caseList)):
        case = caseList[j]
        result = equalIJK(case, qResult, list1)
        output +=  'Case #{0}: {1}\n'.format(j+1,result)
    return output[:-1]

def writeOutput(fileName,output):
    f = open(fileName, 'w')
    f.write(output)

##inputFile = 'test.txt'
##outputFile = 'test_output.txt'

inputFile = 'C.txt'
outputFile = 'C_output.txt'

##inputFile = 'Cb.txt'
##outputFile = 'Cb_output.txt'

qResult = [['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k'],
         ['i', '-1', 'k', '-j', '-i', '1', '-k', 'j'],
         ['j', '-k', '-1', 'i', '-j', 'k', '1', '-i'],
         ['k', 'j', '-i', '-1', '-k', '-j', 'i', '1'],
         ['-1', '-i', '-j', '-k', '1', 'i', 'j', 'k'],
         ['-i', '1', '-k', 'j', 'i', '-1', 'k', '-j'],
         ['-j', 'k', '1', '-i', 'j', '-k', '-1', 'i'],
         ['-k', '-j', 'i', '1', 'k', 'j', '-i', '-1']]
list1 = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']



caseList = readFile(inputFile)
##print caseList
output = solveIt(caseList, qResult, list1)
##print output
writeOutput(outputFile, output)

print 'Done!'
