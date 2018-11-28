def readInput(fileName):
    fileName=open(fileName)
    lists=fileName.read().split()
    
    caseNum=int(lists[0])
    fileName.close()

    pointer=1
    caseList=[]
    
    while pointer<len(lists):     
        case=[]
        case.append(int(lists[pointer]))
        pointer+=1  
        case.append(lists[pointer])
        pointer+=1  
        caseList.append(case)
    return caseNum,caseList

caseNum,caselist=readInput('C:/Users/chao/Desktop/code jam files/2015 qualification/A-small-attempt1.in')

def standingOvation(Smax,audience):
    friend=0
    while True:
        stand=0
        for i in range(Smax):
            if stand>=i:
                stand+=int(audience[i])   
        if stand<Smax:
            friend+=1
            audience=str(int(audience[0])+1)+audience[1:]
        else:return friend

def applyToAllCases(caselist):
    resultlist=[]
    for case in caselist:
        result=standingOvation(case[0],case[1])
        resultlist.append(result)
    return resultlist
    
resultlist=applyToAllCases(caselist)
outFile=open('C:/Users/chao/Desktop/code jam files/2015 qualification/output_small_A.txt','w')
for i in range(caseNum):
    outFile.write("Case #"+str(i+1)+": "+str(resultlist[i]))
    outFile.write('\n')
outFile.close()
