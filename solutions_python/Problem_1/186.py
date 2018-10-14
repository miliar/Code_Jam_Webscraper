import sys
import string

def least(alist):
    minnum=100000
    for each in alist:
        if each<minnum:
            minnum=each
    return minnum

def optimal(queries, engines):
    if len(queries)==0:
        return 0
    length=len(queries)
    numofswitches=[]
    for i in range(len(engines)):
        numofswitches.append(0)
    i=length-1
    while i>=0:
        tmp=[]
        tmp.extend(numofswitches)
        for j in range(len(engines)):
            if queries[i]==engines[j]:
                tmp.pop(j)
                numofswitches[j]=1+least(tmp)
                break
        i-=1
    for j in range(len(engines)):
        if queries[0]==engines[j]:
            numofswitches[j]=100000
    return least(numofswitches)
                
        
inputfile=open(r'.\A-large.in', 'r')
numofcases=string.atoi(inputfile.readline())
for i in range(numofcases):
    numofengines=string.atoi(inputfile.readline())
    engines=[]
    for j in range(numofengines):
        engines.append(inputfile.readline())
    numofqueries=string.atoi(inputfile.readline())
    queries=[]
    for j in range(numofqueries):
        queries.append(inputfile.readline())
    print 'Case #%d: %d' % (i+1, optimal(queries,engines))
