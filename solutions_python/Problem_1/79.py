#!/usr/bin/python2.5

#fileNameInput  = 'A-small.in'
#fileNameOutput = 'A-small.out'
fileNameInput  = 'A-large.in'
fileNameOutput = 'A-large.out'

MAXINT = 2000

def findMax(listToLookIn):
    max = -1
    res = 0
    for x in xrange(len(listToLookIn)):
        if listToLookIn[x] > max:
            max = listToLookIn[x]
            res = x
    return res

def solveProblem(engines, queries):
    switches = 0
    q = queries
    while len(q) > 0:
        ind = [MAXINT]*len(engines)
        qQty = len(q)
        for x in xrange(len(engines)):
            if engines[x] in q: ind[x] = q.index(engines[x])
            else:
                ind[x] = MAXINT
        max = findMax(ind)
        if ind[max] == MAXINT: break
        switches += 1
        q = q[ind[max]:]
    return switches

def writeSolution(file, caseNo, engines, queries):
    file.write('Case #' + str(caseNo) + ': ')
    file.write(str(solveProblem(engines, queries)))
    file.write('\n')

if __name__ == '__main__':
    input = file(fileNameInput, 'r').readlines()
    output = file(fileNameOutput, 'w')

    # filter \n charachters
    for x in xrange(len(input)):
        input[x] = input[x].replace('\r','').replace('\n','')

    numberOfTests = int(input[0])
    line = 1
    for x in xrange(1, numberOfTests+1):
        noS = int(input[line])
        listS = []
        line += 1
        for s in xrange(noS):
            listS.append(input[line])
            line += 1
        noQ = int(input[line])
        listQ = []
        line += 1
        for q in xrange(noQ):
            listQ.append(input[line])
            line += 1
        writeSolution(output, x, listS, listQ)
    output.close()
    print 'done'


