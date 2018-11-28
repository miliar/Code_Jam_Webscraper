file = open("C:\Documents and Settings\davos\Local Settings\Temp\A-small-attempt2.in.txt")
global totalSets
totalSets = int(file.readline())
def getSet():
    i = int(file.readline())
    j = 4-i
    while (i!=1):
        file.readline()
        i -= 1
    firstRowRaw = file.readline()
    while (j!=0):
        file.readline()
        j -= 1
    i = int(file.readline())
    j = 4-i
    while (i!=1):
        file.readline()
        i -= 1
    secondRowRaw = file.readline()
    while (j!=0):
        file.readline()
        j -= 1
    firstRow = [int(firstRowRaw.split()[0]),int(firstRowRaw.split()[1]),int(firstRowRaw.split()[2]),int(firstRowRaw.split()[3])]
    secondRow = [int(secondRowRaw.split()[0]),int(secondRowRaw.split()[1]),int(secondRowRaw.split()[2]),int(secondRowRaw.split()[3])]
    return [firstRow, secondRow]

def checkMatch(dat):
    res = []
    for x in dat[0]:
        for y in dat[1]:
            if x==y:
                res.append(x)
    if len(res)==0:
        return 0
    elif len(res)>=2:
        return -1
    elif len(res)==1:
        return res[0]

def zformat(dat):
    res = ''
    if dat>0:
        res = res + str(dat)
    elif dat==0:
        res = 'Volunteer cheated!'
    elif dat==-1:
        res = 'Bad magician!'
    return res

def output():
    global totalSets
    writes = ''
    caseNo = 1
    while totalSets!=0:
        totalSets -= 1
        writes += 'Case #' + str(caseNo) + ': ' + zformat(checkMatch(getSet())) + '\n'
        caseNo += 1
    outfile = open("C:\Documents and Settings\davos\Local Settings\Temp\A-small-attempt2.out", 'w')
    outfile.write(writes)
