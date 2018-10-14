def readNSolve():
    with open ('B-large.in') as f:
        first=f.readline()
        caseNum=1
        for line in f:
            tidyNum=solve(line)
            writeOutput(caseNum,tidyNum)
            caseNum+=1
def writeOutput(caseNum,tidyNum):
    out = open('B-large.out', 'a')
    out.write('Case #{}: {}\n'.format(caseNum, tidyNum))
def getListInt(line):
    lst=[]
    line=str(line)
    for i in range(len(line)):
        lst.append(int(line[i]))
    return lst

def solve(line):
    intLst = getListInt(int(line))
    while True:
        lstLen = len(intLst)
        stop=True
        for x in range(lstLen-1):
            if((intLst[x]==0) or (intLst[x]>intLst[x+1])):
                stop=False
                intLst[x]-=1
                for j in range(lstLen-x-1):
                    intLst[x+j+1]=9
        for x in range(lstLen):
            if(intLst[x]==0):
                intLst.pop(x)
            else: break
        if(stop==True):
            break
    return "".join(str(x) for x in intLst)
readNSolve()