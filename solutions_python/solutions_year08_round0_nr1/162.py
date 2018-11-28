import string

smax = 100
qmax = 1000

class Engine:
    name = ''
    tempCount = 0
    def __init__(self,str1,i):
        self.name = str1
        self.tempCount = i

arrayEngines = []
for i in range(0,smax):
    engine = Engine('',0)
    arrayEngines.append(engine)

arrayQueries = []
for i in range(0,qmax):
    arrayQueries.append(0)
    
def checkEngineTagFull(n):
    for i in range (0,n):
        if arrayEngines[i].tempCount == 0:
            return 0
    return 1

def flushEngineTag(n,m):
    for i in range(0,n):
        arrayEngines[i].tempCount = 0
    arrayEngines[m].tempCount = 1
    

f = open('C:\\Users\\Moose\Desktop\\A-large.in','r')
nbCases = int(f.readline())
for caseNb in range(0,nbCases):
    nbSwitch = 0
    nbEngines = int(f.readline())
    for i in range(0,nbEngines):
        arrayEngines[i].name = string.strip(f.readline())
        arrayEngines[i].tempCount = 0

    nbQueries = int(f.readline())
    for i in range(0,nbQueries):
        queryStr = string.strip(f.readline())
        ifMatch = 0
        for j in range(0,nbEngines):
            if (queryStr == arrayEngines[j].name):
                arrayQueries[i]=j
                ifMatch = 1
                break
        if ifMatch == 0:
            print "Zut... %d" % i
    for i in range(0,nbQueries):
        arrayEngines[arrayQueries[i]].tempCount += 1
        if checkEngineTagFull(nbEngines) == 1:
            nbSwitch += 1
            flushEngineTag(nbEngines,arrayQueries[i])

    print "Case #" + str(caseNb+1) + ": " + str(nbSwitch)

f.close()

