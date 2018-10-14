def calculateIncome(numRides,capacity,gc,groupsString):
    g=map(eval,groupsString)
    print g
    profit=0
    q=0
    for i in range(0,numRides):
        pob=0
        for j in range(0, gc):
            group=g[q%gc]
            if pob+group<=capacity:
                pob+=group
                q+=1
            else:
                break
        profit+=pob
    print profit
    return profit
        

def solveProblem():
    fIn=open('C-Small.in.txt', 'r')
    fOut=open('C-Small.out', 'w')
    numCases=int(fIn.readline())
    print numCases
    for i in range(0,numCases):
        specs=fIn.readline()
        specParts=specs.rsplit(' ')
        numRides=int(specParts[0])
        capacity=int(specParts[1])
        groupCount=int(specParts[2])
        groupInfo=fIn.readline()
        groups=groupInfo.rsplit(' ')
        numEuros=calculateIncome(numRides,capacity,groupCount,groups)
        fOut.write('Case #')
        fOut.write(str(i+1))
        fOut.write(': ')
        fOut.write(str(numEuros))
        fOut.write('\n')
    fIn.close()
    fOut.close()
                


if __name__=="__main__":
    solveProblem()
