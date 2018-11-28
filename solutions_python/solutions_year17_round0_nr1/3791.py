def readNSolve():
    with open ('A-large.in') as f:
        first=f.readline()
        caseNum=1
        for line in f:
            flipNum=solve(line)
            writeOutput(caseNum,flipNum)
            caseNum+=1
def writeOutput(caseNum,flipNum):
    out = open('A-large.out', 'a')
    out.write('Case #{}: {}\n'.format(caseNum, flipNum)) if flipNum >= 0 \
        else out.write('Case #{}: {}\n'.format(caseNum, 'IMPOSSIBLE'))
def switchCake(signal):
    return '+' if signal=='-' else '-'
def solve(line):
    numswitch=0
    splits=line.split(" ")
    flipNum=int(splits[1])
    cake=list(splits[0])
    i=0
    cakelen=len(cake)
    while(cakelen>=(i+flipNum)):
        if(cake[i]=='-'):
            numswitch+=1
            for j in range(flipNum):
                cake[j+i]=switchCake(cake[j+i])
        i+=1
    if(cake.count('-')>0):
        numswitch=-1
    return numswitch
readNSolve()